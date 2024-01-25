from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from configs.Database import (
    get_db_connection
)
from models.QomplntModel import QomplntQr, MultiLingualText, Location, B2BTenant
from scripts.dml import DMLScript



class QomplantQeRepositry:
    db : Session
    def __init__(self, db: Session = Depends(get_db_connection)) -> None:
        self.db = db

    def create(self, qomplntqr: QomplntQr) -> QomplntQr:
        location_id = qomplntqr.location_id
        b2b_tenant_id = qomplntqr.b2b_tenant_id
        exist_location  = self.db.query(Location).filter(Location.id == location_id).first()
        exist_b2btenant  = self.db.query(Location).filter(B2BTenant.id == b2b_tenant_id).first()
        if not (exist_location and exist_b2btenant):
            raise HTTPException(status_code=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION, detail= f"Location with ID {location_id} and B2b Tenant {b2b_tenant_id} does not exist.")

        params = {
            'location_id': qomplntqr.location_id,
            'uuid': qomplntqr.uuid,
            'b2b_tenant_id': qomplntqr.b2b_tenant_id,
            'ml_quote': qomplntqr.ml_quote,
            'ml_sub_text': qomplntqr.ml_sub_text,
            'sub_media': qomplntqr.sub_media
        }
        print("city table", qomplntqr.__tablename__)
        # print("params", params)
        data = DMLScript(db=self.db).dml_insert(qomplntqr.__tablename__,params)
        print("____________________________________________________________________________________________________")
        print("Columns Values:  ",  data )
        responce = {
            "data":data,
            "message":"qomplntqr table has been created"
        }    
        return responce

   
    def get(self, lang_code: int, qomplnt_uuid: str) -> QomplntQr:
        # qomplntor = self.db.query(QomplntQr).filter(QomplntQr.uuid == qomplnt_uuid).first()
        # qomplntors = self.db.query(QomplntQr).join(Location, QomplntQr.location).join(B2BTenant, QomplntQr.b2b_tenant).filter(QomplntQr.uuid == qomplnt_uuid).options(joinedload(QomplntQr.location)).all()
        # data = self.db.query(B2BTenant).join(Location, B2BTenant.location).filter(Location.id == b2b_id).options(joinedload(B2BTenant.location)).all()
        qomplntors = self.db.query(QomplntQr).join(Location, QomplntQr.location).join(B2BTenant, QomplntQr.b2b_tenant).filter(QomplntQr.uuid == qomplnt_uuid).options(joinedload(QomplntQr.location), joinedload(QomplntQr.b2b_tenant)).all()

      
        

        lang_code = self.db.query(MultiLingualText).filter(MultiLingualText.lang_code == lang_code).first()
        if lang_code is None or qomplntors is None:
        # Raise an exception or return an error response
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid lang code or uuid")
        # print("lang code",{"lang_code":lang_code.lang_code, "Key":lang_code.keys})
        # print('result-->', qomplntor.location.address1)
        # print("b2b_tenant_id", qomplntor.b2b_tenant.id) 
        result_list = []
        for qomplntor in qomplntors:   
            location = {
            "id": qomplntor.location.id,
            "geo_id": qomplntor.location.geo_id,
            "address1": qomplntor.location.address1,
            "address2": qomplntor.location.address2,
            "landmark": qomplntor.location.landmark,
            "city_id": qomplntor.location.city_id,
            "zip_code": qomplntor.location.zip_code
                }
            b2b_tenant = {
                "id": qomplntor.b2b_tenant.id,
                "name": qomplntor.b2b_tenant.name,
                "ml_name": qomplntor.b2b_tenant.ml_name,
                "location_id": qomplntor.b2b_tenant.location_id,
                "media": qomplntor.b2b_tenant.media,            
            }
            data = {
            "id": qomplntor.id,
            "b2b_tenant_id": qomplntor.b2b_tenant_id,
            "ml_quote": qomplntor.ml_quote,
            "sub_media": qomplntor.sub_media,
            "ml_sub_text": qomplntor.ml_sub_text,
            "location_id": qomplntor.location_id,  # Add location_id if it's a required field
            "location": [location],
            "b2b_tenant": [b2b_tenant]
            }
        result_list.append(data)
        return result_list



    # def get(self, lang_code: int, qomplnt_uuid: str) -> QomplntQr:
    #     # qomplntor = self.db.query(QomplntQr).filter(QomplntQr.uuid == qomplnt_uuid).first()
    #     qomplntor = self.db.query(QomplntQr).filter(QomplntQr.uuid == qomplnt_uuid).first()

    #     lang_code = self.db.query(MultiLingualText).filter(MultiLingualText.lang_code == lang_code).first()
    #     if lang_code is None or qomplntor is None:
    #     # Raise an exception or return an error response
    #         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid lang code or uuid")
    #     print("lang code",{"lang_code":lang_code.lang_code, "Key":lang_code.keys})
    #     print('result-->', qomplntor.location.address1)
    #     print("b2b_tenant_id", qomplntor.b2b_tenant.id)    
    #     location = {
    #     "id": qomplntor.location.id,
    #     "geo_id": qomplntor.location.geo_id,
    #     "address1": qomplntor.location.address1,
    #     "address2": qomplntor.location.address2,
    #     "landmark": qomplntor.location.landmark,
    #     "city_id": qomplntor.location.city_id,
    #     "zip_code": qomplntor.location.zip_code
    #         }
    #     b2b_tenant = {
    #         "id": qomplntor.b2b_tenant.id,
    #         "name": qomplntor.b2b_tenant.name,
    #         "ml_name": qomplntor.b2b_tenant.ml_name,
    #         "location_id": qomplntor.b2b_tenant.location_id,
    #         "media": qomplntor.b2b_tenant.media,            
    #     }
    #     data = {
    #     "id": qomplntor.id,
    #     "b2b_tenant_id": qomplntor.b2b_tenant_id,
    #     "ml_quote": qomplntor.ml_quote,
    #     "sub_media": qomplntor.sub_media,
    #     "ml_sub_text": qomplntor.ml_sub_text,
    #     "location_id": qomplntor.location_id,  # Add location_id if it's a required field
    #     "location": [location],
    #     "b2b_tenant": [b2b_tenant]
    #     }
    #     return [data]
    
    