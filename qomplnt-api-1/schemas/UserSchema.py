from pydantic import BaseModel

class UserSchema(BaseModel):
    name: str
    email: str
    password: str


class LoginSchema(BaseModel):
    email:str
    password:str
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
    email: str

    class Config:
        orm_mode = True 

      

    


    