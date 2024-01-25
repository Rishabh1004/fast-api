from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from configs.Database import (
    get_db_connection
)
from models.QomplntModel import MultiLingualText
from scripts.dml import DMLScript


class MLTextRepositry:
    db : Session
    def __init__(self, db: Session = Depends(get_db_connection)) -> None:
        self.db = db

    def create(self, mltext: MultiLingualText) -> MultiLingualText:
        params = {
            'keys': mltext.keys,
            'lang_code': mltext.lang_code,
            'display_text': mltext.display_text
        }

        data = DMLScript(db=self.db).dml_insert(mltext.__tablename__,params)
        print("____________________________________________________________________________________________________")
        print("Columns Values:  ",  data )
        responce = {
            "data":data,
            "message":"Multi Lingual Text table  has been created"
        }    
        return responce
        # self.db.execute(sql, params)
        # self.db.commit()
        # return mltext