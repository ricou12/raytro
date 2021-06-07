from utils.db import DB
from utils import security
from models.User import User
from models.Feedback import Feedback

db = DB()


def check_credentials(login_or_token: str, password: str or None) -> User or False:
    """Vérifie la validité des login/pass (ou du token) de l'utilisateur

    :param login_or_token:
        soit le login spécifié par l'utilisateur,
        soit le token qui lui a été fourni par l'application
    :param password:
        le mot de passe en clair de l'utilisateur
    :return:
        L'objet User correspondant si les credentials sont valides, False sinon !

    Si le password est vide, on considère que c'est un token qui est passé en paramètre
    Sinon, on considère que c'est une paire login/pass
    """
    return db.check_credentials(login_or_token, password)


def generate_access_token(user):
    return security.generate_access_token(user)


def create_user(first_name: str, email: str, clear_password: str, is_admin: bool = False) -> bool:
    return db.create_user(first_name, email, clear_password, is_admin)


def create_feedback(feedback: Feedback):
    return db.create_feedback(feedback)


def get_feedbacks(year: int, week: int):
    return db.get_feedbacks(year, week)
