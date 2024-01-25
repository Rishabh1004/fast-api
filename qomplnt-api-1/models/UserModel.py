from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from .BaseModel import EntityMeta


class User(EntityMeta):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    email = Column(String(255), unique=True, index= True)
    password = Column(String(255), index=True) 