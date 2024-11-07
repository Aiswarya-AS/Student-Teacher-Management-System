

import hashlib


def hash_password(password):
    """
    Hashes a password using SHA256.
    """
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password
