from passlib.hash import pbkdf2_sha256

def is_authenticate(user, password):
    user_password = user.password
    return pbkdf2_sha256.verify(password, user_password)