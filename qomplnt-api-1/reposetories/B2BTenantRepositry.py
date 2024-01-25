from fastapi import Depends
from sqlalchemy.orm import Session, joinedload
from configs.Database import get_db_connection
from models.QomplntModel import B2BTenant, Location
from scripts.dml import DMLScript



class B2BTenantRepositry:
    db: Session

    def __init__(self, db: Session = Depends(get_db_connection)) -> None:
        self.db = db

    def create(self, b2btenant: B2BTenant) -> B2BTenant:

        params = {
            'name': b2btenant.name,
            'ml_name': b2btenant.ml_name,
            'location_id': b2btenant.location_id,
            'media': b2btenant.media,
        }
        print("city table", b2btenant.__tablename__)
        # print("params", params)
        data = DMLScript(db=self.db).dml_insert(b2btenant.__tablename__,params)
        print("____________________________________________________________________________________________________")
        print("Columns Values:  ",  data )
        responce = {
            "data":data,
            "message":"b2bteant table has been created"
        }    
        return responce


    def get(self, b2b_id: int) -> B2BTenant:
        data = self.db.query(B2BTenant).join(Location, B2BTenant.location).filter(Location.id == b2b_id).options(joinedload(B2BTenant.location)).all()
        print(data)
        result_list = []
        for b2btenant in data:
            # Format location data
            location = {
                "id": b2btenant.location.id,
                "geo_id": b2btenant.location.geo_id,
                "address1": b2btenant.location.address1,
                "address2": b2btenant.location.address2,
                "landmark": b2btenant.location.landmark,
                "city_id": b2btenant.location.city_id,
                "zip_code": b2btenant.location.zip_code,
            }

            # Format B2BTenant data
            b2btenant_data = {
                "id": b2btenant.id,
                "name": b2btenant.name,
                "ml_name": b2btenant.ml_name,
                "location_id": b2btenant.location_id,
                "media": b2btenant.media,
                "location": [location]
            }

            # Append the formatted data to the result list
        result_list.append(b2btenant_data)

        # Return the final result list
        return result_list
       
