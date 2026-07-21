from passlib.context import CryptContext
pwd_context= CryptContext(schemes=["bcrypt"],deprecated="auto") #bcrypt== "pip install bcrypt==4.0.1"

def get_pwdhash(pwd:str)-> str:
    return pwd_context.hash(pwd)

def varify_pwd(pwd:str,hashed_pwd:str)-> bool:
    return pwd_context.verify(pwd,hashed_pwd)

user_pwd= "123"   #sign up
print(f"original Password:{user_pwd}")  #plain pass

hash_pwd = get_pwdhash(user_pwd)
print(f"Hashed password Stored in Db:{hash_pwd}")

login_atempt = "123"
is_valid= varify_pwd(login_atempt,hash_pwd) # checking after/ while logging
print(f"Login Attempt with:{login_atempt} is_valid:{is_valid}")

login_atempt1 = "1234"
is_valid1 = varify_pwd(login_atempt1,hash_pwd) # checking after/ while logging
print(f"Login Attempt with:{login_atempt1} is_valid:{is_valid1}")

