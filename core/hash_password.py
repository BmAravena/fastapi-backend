from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError



pwd_hasher = PasswordHasher()


def hash_password(password: str) -> str:
    return pwd_hasher.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    try:
        return pwd_hasher.verify(hashed, plain)
    except VerifyMismatchError:
        return False