from pwdlib import PasswordHash


password_hash_instance = PasswordHash.recommended()

def hash_password(password:str)->str:
    return password_hash_instance.hash(password)

def verify_and_update_password(plain_password:str, hashed_password:str)->tuple[bool, str|None]:
    return password_hash_instance.verify_and_update(plain_password, hashed_password)


def verify_password(plain_password:str, hashed_password:str)->bool:
    return password_hash_instance.verify(plain_password, hashed_password)