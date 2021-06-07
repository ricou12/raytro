import os
import psycopg2
import bcrypt
import pathlib
from dotenv import load_dotenv
from datetime import datetime
from pprint import pprint
from models.User import User
from models.Feedback import Feedback


class DB:
    """Genre de driver~API pour notre application."""

    def __init__(self):
        load_dotenv()
        DB_HOST = os.getenv('DB_HOST')
        DB_PORT = os.getenv('DB_PORT')
        DB_USER = os.getenv('DB_USER')
        DB_PASSWORD = os.getenv('DB_PASSWORD')
        DB_NAME = os.getenv('DB_NAME')
        self.conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD, dbname=DB_NAME)
        self.cur = self.conn.cursor()

    def setup(self, drop_if_exists=False):
        """Crée la BDD nécessaire pour faire tourner notre application

        Crée toutes les tables et types nécessaires, puis insère les entrées nécessaires au bon fonctionnement (
        administrateur par défaut par exemple)

        :param drop_if_exists
        Supprime tout de la base avant (tables et type pour le moment)
        """
        setup_file_path = find('setup.sql', pathlib.Path().absolute())
        truncate_file_path = find('truncate_database.sql', pathlib.Path().absolute())

        if drop_if_exists:
            with open(truncate_file_path) as f:
                self.cur.execute(f.read())
        with open(setup_file_path) as f:
            self.cur.execute(f.read())
            self.conn.commit()

    def create_user(self, first_name, email, clear_password, is_admin=False) -> bool:
        encrypted_password = bcrypt.hashpw(clear_password.encode('UTF-8'), bcrypt.gensalt(13)).decode('UTF-8')
        try:
            self.cur.execute('INSERT INTO Users (firstname, email, password, isadmin) VALUES (%s, %s, %s, %s)',
                         (first_name, email, encrypted_password, is_admin))
            self.conn.commit()
            return True
        except Exception as e:
            self.conn.rollback()
        return False

    def check_credentials(self, login: str, clear_password: str) -> User  or False:
        self.cur.execute(f'SELECT * FROM Users WHERE email = \'{login}\'')
        result = self.cur.fetchone()
        pprint(result)
        if len(result) and bcrypt.checkpw(clear_password.encode('UTF-8'), result[3].encode('UTF-8')):
            return User(result[1], result[2], result[3], result[4], '')
        else:
            return False

    def get_users(self):
        self.cur.execute('SELECT firstname, email, isadmin FROM Users')
        return self.cur.fetchmany()

    def create_feedback(self, feedback: Feedback) -> bool:
        feedback_items = []
        week_number = datetime.now().date().isocalendar()[1]
        year = datetime.now().date().year

        for item in feedback.liked:
            feedback_items.append((year, week_number, 'liked', item))
        for item in feedback.disliked:
            feedback_items.append((year, week_number, 'disliked', item))

        try:
            self.cur.executemany('INSERT INTO FEEDBACKS (year, week, type, message) VALUES(%s, %s, %s, %s)', feedback_items)
            self.conn.commit()
        except Exception:
            return False
        return True

    def get_feedbacks(self, year: int, week: int):
        self.cur.execute('SELECT * FROM Feedbacks WHERE year = %s AND week = %s', (year, week))
        return self.cur.fetchall()


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


if __name__ == '__main__':
    db = DB()
    db.setup(drop_if_exists=True)
    db.create_user('bobrazowsky', 'bob@mac.sa', 'afzrgfzg')
    db.create_user('bobrazowskyII', 'bob@mac2.sa', 'afzrgfzg')
    db.create_user('bobrazowskyIII', 'bob@mac3.sa', 'afzrgfzg')
