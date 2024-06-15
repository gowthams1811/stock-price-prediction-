import bcrypt

users_db = {}

def register_user(username, password):
    if username in users_db:
        return False
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    users_db[username] = hashed_pw
    return True

def check_credentials(username, password):
    if username in users_db:
        return bcrypt.checkpw(password.encode(), users_db[username])
    return False