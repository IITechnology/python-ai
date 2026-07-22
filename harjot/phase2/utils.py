from passlib.context import CryptContext
pwd_context= CryptContext(schemes=["bcrypt"],deprecated="auto") #bcrypt== "pip install bcrypt==4.0.1"

def get_pwdhash(pwd:str)-> str:
    return pwd_context.hash(pwd)

def varify_pwd(pwd:str,hashed_pwd:str)-> bool:
    return pwd_context.verify(pwd,hashed_pwd)

