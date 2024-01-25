# from passlib.context import CryptContext
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Union

# # openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30



# Function to create a JWT token
def create_jwt_token(data: dict, expires_delta: timedelta = None):
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
        
    to_encode = data.copy()
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt











# # # Function to authenticate user and generate token
# # def authenticate_user(username: str, password: str):
# #     user = users.get(username)
# #     if user and pwd_context.verify(password, user["password"]):
# #         access_token_expires = timedelta(minutes=30)  # Set token expiration time
# #         access_token = create_access_token(data={"sub": username}, expires_delta=access_token_expires)
# #         return {"access_token": access_token, "token_type": "bearer"}

# #     return None

