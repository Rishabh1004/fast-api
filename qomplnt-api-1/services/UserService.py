from typing import List, Optional

from fastapi import Depends, HTTPException, status
from models.UserModel import User
from hash.hashing import Hash 

from reposetories.UserReposetry import UserRepository
from schemas.UserSchema import UserSchema,LoginSchema



class UserService:
    userRepository: UserRepository

    def __init__(
            self, userRepository: UserRepository = Depends()
    ) -> None:
        self.userRepository = userRepository

    def create(self, user_body: UserSchema) -> User:
        return self.userRepository.create(
            User(name=user_body.name, email= user_body.email, password=user_body.password)
        )
        
    
 
    def get(self, user: User) -> User:
        fetched_user = self.userRepository.get(user)
        print(f"Returned user data: {fetched_user}")  # Add this line for debugging
        return fetched_user
    
    # def login(self, user: LoginSchema) -> Optional[User]:
    #     return self.userRepository.login(user = {'email':user.email,'password':user.password})
    
    def login(self, login_data: LoginSchema) -> User:
        
        user = self.userRepository.login(login_data.email, login_data.password)
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        return user    