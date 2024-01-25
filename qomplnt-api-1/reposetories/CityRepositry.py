from fastapi import Depends
from sqlalchemy.orm import Session
from configs.Database import (
    get_db_connection
)
from sqlalchemy import text
from models.QomplntModel import City
from scripts.dml import DMLScript


class CityRepositry:
    db : Session
    def __init__(self, db: Session = Depends(get_db_connection)) -> None:
        self.db = db

    def create(self, city: City):
        
        params = {
            'city': city.city,
            'district': city.district,
            'state': city.state,
            'country': city.country
        }
        print("city table", city.__tablename__)
        # print("params", params)
        data = DMLScript(db=self.db).dml_insert(city.__tablename__,params)
        print("____________________________________________________________________________________________________")
        print("Columns Values:  ",  data )
        responce = {
            "data":data,
            "message":"City has been created"
        }    
        return responce
