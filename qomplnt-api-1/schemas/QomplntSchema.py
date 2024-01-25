from pydantic import BaseModel,  ValidationError, validator
from typing import List, Optional
from pydantic import ConfigDict
class OurBaseModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

class QomplantQrSchema(BaseModel):
    # uuid: str
    location_id: int
    b2b_tenant_id: int
    ml_quote: str = None
    ml_sub_text: str = None
    sub_media: str = None

class B2bTenantSchema(BaseModel):
    name: str
    ml_name: str = None
    location_id: int = None
    media: str = None
    class Config():
        orm_mode = True

class LocationSchema(BaseModel):
  
    geo_id: dict = None
    address1: str = None
    address2: str = None
    landmark: str = None
    city_id: int
    zip_code:int
    class Config():
        orm_mode = True

    @validator("geo_id","address1", pre=True, always=True)
    
    def check_empty_string(cls, value):
        if not value:
            raise ValueError("Field cannot be an empty string")
        return value
    @validator('city_id')
    def check_positive_integer(cls, value):
        if value < 0:
            raise ValueError("Value should be iteger ")
        return value

class B2bTenantLocationSchema(BaseModel):
    name: str
    ml_name: str = None
    location_id: int = None
    media: str = None
    location :Optional[List[LocationSchema]] = []
    class Config():
        orm_mode = True


class QomplantQrLocationSchema(BaseModel):
    # uuid: str
    location_id: int
    b2b_tenant_id: int
    ml_quote: str = None
    ml_sub_text: str = None
    sub_media: str = None
    location: Optional[List[LocationSchema]]=[] 
    b2b_tenant:Optional[List[B2bTenantSchema]]=[] 
    class Config():
        orm_mode = True

        
  

class MultiLingualTextSchema(BaseModel):
    # int: int
    keys: int
    lang_code: int
    display_text: str

    @validator("keys", "lang_code")
    def check_positive_integer(cls, value):
        if value < 0:
            raise ValueError("Value should be iteger ")
        return value

class CitySchema(BaseModel):

    city: str
    district: str
    state: str
    country: str

    @validator("city", "district","state", "country", pre=True, always=True)
    def check_empty_string(cls, value):
        if not value:
            raise ValueError("Field cannot be an empty string")
        return value
    






class DMLResponce(BaseModel):
    data:dict
    message :str    