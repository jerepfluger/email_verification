import hashlib
from os import environ as env


def password_encryptor(password):
    encoded_password = f'{password}{env["SALT"]}'.encode()
    return hashlib.sha3_512(encoded_password).hexdigest()
