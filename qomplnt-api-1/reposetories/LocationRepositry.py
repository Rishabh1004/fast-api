from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import text
from configs.Database import (
    get_db_connection
)
from models.QomplntModel import Location
from scripts.dml import DMLScript


class LocationRepositry:
    db : Session
    def __init__(self, db: Session = Depends(get_db_connection)) -> None:
        self.db = db

    def create(self, location: Location) -> Location:
        print("Length----",len(str(location.zip_code)))
        if len(str(location.zip_code)) != 6:
            raise HTTPException(
            status_code=status.HTTP_206_PARTIAL_CONTENT,
            detail=f"The zip code {location.zip_code} is invalid. It should be exactly 6 digits."
        )
        # self.db.add(location)
        # self.db.commit()
        # self.db.refresh(location)
        # return location  
        # sql = text("""
            # INSERT INTO location (geo_id, address1, address2, landmark, city_id, zip_code)
            # VALUES (:geo_id, :address1, :address2, :landmark, :city_id, :zip_code)
        # """)
 
        params = {
            'geo_id': location.geo_id,
            'address1': location.address1,
            'address2': location.address2,
            'landmark': location.landmark,
            'city_id': location.city_id,
            'zip_code': location.zip_code
        }
  
        data = DMLScript(db=self.db).dml_insert(location.__tablename__,params)
        print("____________________________________________________________________________________________________")
        print("Columns Values:  ",  data )
        responce = {
            "data":data,
            "message":"Location table  has been created"
        }    
        return responce
         