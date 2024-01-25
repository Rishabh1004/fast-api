from fastapi import Depends, HTTPException, status
from models.QomplntModel import QomplntQr
from reposetories.QomplntQrRepositry import QomplantQeRepositry
from schemas.QomplntSchema import QomplantQrSchema





class QomplantQrService:
    qomplantReposetry: QomplantQeRepositry

    def __init__(
            self, qomplantReposetry: QomplantQeRepositry = Depends()
    ) -> None:
        self.qomplantReposetry = qomplantReposetry

    def create(self, qomplantqr_body: QomplantQrSchema) -> QomplntQr:
        qomplantqr = self.qomplantReposetry.create(            
            QomplntQr(
                location_id = qomplantqr_body.location_id,
                b2b_tenant_id= qomplantqr_body.b2b_tenant_id,
                ml_quote = qomplantqr_body.ml_quote,
                ml_sub_text = qomplantqr_body.ml_sub_text,
                sub_media = qomplantqr_body.sub_media
            )
        )
        return [qomplantqr]
        

   

    def get(self, lang_code: int, qomplnt_uuid: str) -> QomplntQr:
        return self.qomplantReposetry.get(lang_code, qomplnt_uuid)
    
    

        

