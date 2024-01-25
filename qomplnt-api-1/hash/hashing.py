from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated="auto")

class Hash():
    
    def bycrypt(password):
        pwd_cxt.hash(password)
    
    def verify(hashed_password, plane_password):
        pwd_cxt.verify(plane_password , hashed_password)