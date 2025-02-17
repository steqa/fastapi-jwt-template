from cryptography.fernet import Fernet

from api.settings import settings

with open(settings.PASSWORD_SECRET_KEY_PATH, "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)


def encrypt_password(password: str) -> bytes:
    return cipher.encrypt(password.encode())


def decrypt_password(encrypted_password: bytes) -> str:
    return cipher.decrypt(encrypted_password).decode()


def verify_password(plain_password: str, hashed_password: bytes) -> bool:
    return plain_password == decrypt_password(hashed_password)
