from flask import Flask, jsonify, request, Response
import bcrypt
from os import getenv
from pprint import pprint
from dotenv import load_dotenv
from controllers import index as core_controllers
from models.response import StaticCodes
from models.Feedback import Feedback
from utils.security import check_access_token, setup as security_setup
from utils.db import DB

app = Flask(__name__)


@app.route('/')
def root():
    return 'le serveur fonctionne !'


@app.route('/register', methods=['POST'])
def register():
    return jsonify(StaticCodes.work_in_progress)


@app.route('/login', methods=['POST'])
def login():

    email = request.get_json().get('login') if request.get_json().get('login') else ''
    password = request.get_json().get('password') if request.get_json().get('password') else ''
    # core_controllers.create_user('Renaud', 'contact@asciiparait.fr', 'soupaSikrait', True)
    if user := core_controllers.check_credentials(email, password):
        return jsonify({
            'status': 'success',
            'access_token': core_controllers.generate_access_token(user),
            'description': 'Identifiants valides, vous être maintenant connecté'
        })
    return jsonify(StaticCodes.wrong_credentials)


@app.route('/signup', methods=['POST'])
def signup():
    email = request.get_json().get('login') if request.get_json().get('login') else ''
    first_name = request.get_json().get('login') if request.get_json().get('login') else ''
    password = request.get_json().get('password') if request.get_json().get('password') else ''

    # Création du compte + tentative de connexion comme si de rien n'était !
    if core_controllers.create_user(email, first_name, password, False):
        return login()
    return jsonify(StaticCodes.account_creation_error)


@app.route('/feedback', methods=['GET', 'POST'])
@app.route('/feedback/<int:year>/<int:week>', methods=['GET'])
def feedback(year: int or None = None, week: int or None = None):
    if request.method == 'GET':
        return jsonify(core_controllers.get_feedbacks(year, week))
    elif request.method == 'POST':
        # Todo: rendre possible l'insertion en tenant compte de l'année/semaine passée ? (pas sûr que ce soit malin)
        feed = Feedback(request.get_json().get('liked'), request.get_json().get('disliked'))
        if core_controllers.create_feedback(feed):
            return StaticCodes.default_success, 201
        return StaticCodes.default_error, 500


@app.route('/show-participants')
def show_participants():
    return jsonify(StaticCodes.work_in_progress)


@app.before_request
def logger():
    if request.method != 'OPTIONS':
        print('[info] request on ' + request.method + ' - ' + request.path)


@app.before_request
def handle_credentials():
    unprotected_endpoints = [
        '/login',
        '/signup',
    ]
    if request.method == 'OPTIONS':
        return StaticCodes.work_in_progress, 204
    if request.path not in unprotected_endpoints:
        print('[INFO] protected endpoint: check credentials')
        if not request.headers.get('Authorization') or len(request.headers.get(
                'Authorization')) < 5:
            print('[INFO] ... No credentials provided, request ended')
            return StaticCodes.default_error, 400
        auth_type, credentials = tuple(str(request.headers.get('Authorization', type=str)).split(' '))

        if auth_type == "Bearer" and (_ := check_access_token(credentials)):
            print('[INFO] valid bearer provided')
        else:
            print('[WARN] invalid credentials')
            return jsonify(StaticCodes.default_error), 403


@app.after_request
def enable_cors(response: Response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'PATCH, PUT, GET, POST, DELETE, OPTIONS')
    response.headers.add('Content-Type', '*/*')
    response.headers.add('Access-Control-Allow-Headers', 'X-Custom-Header, Content-Type, Authorization')
    return response


if __name__ == "__main__":
    load_dotenv()
    host = getenv('SERVER_HOST') if getenv('SERVER_HOST') else '0.0.0.0'
    port = int(getenv('SERVER_PORT')) if getenv('SERVER_PORT') else 80
    debug = bool(getenv('DEBUG')) if getenv('DEBUG') else False
    setup = bool(getenv('RAYTRO_SETUP')) if getenv('RAYTRO_SETUP') else False

    if setup:
        print('Setup')
        db = DB()
        db.setup()
        security_setup()
    app.run(host=host, port=port, debug=debug)
