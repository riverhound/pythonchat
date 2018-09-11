import hashlib

def get_hash(login, level, password):

    msg = hashlib.sha256()

    msg.update(login.encode())
    msg.update(level.encode())
    msg.update(password.encode())

    h = msg.hexdigest()

    return h

