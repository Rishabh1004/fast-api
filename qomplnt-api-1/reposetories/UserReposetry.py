from typing import List, Optional
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session, lazyload
from hash.hashing import Hash
from passlib.context import CryptContext
from jwt.jwt_token import create_jwt_token
from passlib.context import CryptContext
from datetime import  timedelta
from typing import List




from configs.Database import (
    get_db_connection
)
from models.UserModel import User


# Create an instance of CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserRepository:
    db :Session

    def __init__(self, db: Session = Depends(get_db_connection)) -> None:
        self.db = db
        

    def get(self, user:User) -> User:
        user = self.db.query(User).all()
        return user


    

    def create(self, user: User) -> User:
        existing_user = self.db.query(User).filter(User.email == user.email).first()
        if existing_user:
            # If user already exists, raise an HTTPException or return False
            raise HTTPException(status_code=400, detail="User already exists")
        # Hash the password before storing it
        hashed_password = pwd_context.hash(user.password)
        user.password = hashed_password
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    

    

    def login(self, email: str, password: str) -> dict:
        user = self.db.query(User).filter(User.email == email).first()
        if not user or not pwd_context.verify(password, user.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

        # Example data for the token payload
        token_data = {"sub": user.email}

        # Generate a token with a 30-minute expiration
        access_token = create_jwt_token(token_data, expires_delta=timedelta(minutes=30))
        token_response = {
            "access_token": access_token,
            "token_type": "bearer",
            "email": user.email
        }
        
        return [token_response]   
        


    
        

