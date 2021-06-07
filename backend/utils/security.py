from models.User import User
from os import system, remove
import pathlib
import jwt

# TODO: trouver une meilleure solution pour enregistrer à la racine du back que ce replace moisi
PRIVATE_KEY_PATH = f'{pathlib.Path().absolute()}/id_rsa'.replace('/utils', '')
PUBLIC_KEY_PATH = f'{pathlib.Path().absolute()}/id_rsa.pub'.replace('/utils', '')


def setup():
    print('-- Génération de la clé RSA')
    rotate_keys()


def rotate_keys():
    if pathlib.Path(PRIVATE_KEY_PATH).is_file():
        remove(PRIVATE_KEY_PATH)
        remove(PUBLIC_KEY_PATH)

    system(f'openssl genpkey -out {PRIVATE_KEY_PATH} -algorithm RSA -pkeyopt rsa_keygen_bits:2048')
    system(f' openssl rsa --in {PRIVATE_KEY_PATH} --outform PEM -pubout -out {PUBLIC_KEY_PATH}')


def generate_access_token(user: User):
    private_key: bytes

    with open(PRIVATE_KEY_PATH, 'r') as f:
        private_key = f.read().encode('UTF-8')
    token = jwt.encode(user.__dict__, private_key, algorithm='RS256')
    return token


def check_access_token(token: str) -> dict or False:
    public_key: bytes

    with open(PUBLIC_KEY_PATH, 'r') as f:
        public_key = f.read().encode('UTF-8')
    try:
        return jwt.decode(token, public_key, algorithms=['RS256'])
    except jwt.exceptions.InvalidSignatureError:
        return False


if __name__ == '__main__':
    setup()
    toktok = generate_access_token(User('Jean', 'jean@hotmail.fr', 'zgergerg', access_token='', is_admin=''))
    print(toktok)
    check_access_token(toktok)
    check_access_token('eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJmaXJzdF9uYW1lIjoiSmVhbiIsImVtYWlsIjoiamVhbkBob3RtYWlsLmZyIiwiZW5jcnlwdGVkX3Bhc3N3b3JkIjoiemdlcmdlcmciLCJpc19hZG1pbiI6IiIsImFjY2Vzc190b2tlbiI6IiJ9.xZ1n_j47JlB8nPGHMrr8ImEiT3kbKIHrkyZHTkPQ3y7yW_DkvyF3alPhhglJzU1r1tFunbeCAfiLgTaJslSEKuHmfjnnsJQUcvYyfOtyNzFqtcVUEJ2lCb-Fi_ZZiB02PBsacRAEqiWVp9irIf6qUs_oCudf8_ndoL1441gg1uD38oYUKrKZ0gSThaOBg6vcoyw_nIl_em14NWkIcn-v3YGzgIhJPM13v_psUQXHRvCboaT9eGs5r-0pAbrAc5V0PXSrSfh54kxTGZjZ3uNE7tzwGXsCqnhsKE34v6AWsxBqHeamJVS_xT--8Do_uAOYTEYMZCI1UFQlBwLOTH9sIA'
)
