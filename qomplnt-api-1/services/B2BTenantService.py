from typing import List, Optional

from fastapi import Depends, HTTPException, status
from models.QomplntModel import B2BTenant
from reposetories.B2BTenantRepositry import B2BTenantRepositry
from schemas.QomplntSchema import B2bTenantSchema
from models.QomplntModel import Location




class B2BTenantService:
    b2btenantReposetry: B2BTenantRepositry

    def __init__(
            self, b2btenantReposetry: B2BTenantRepositry = Depends()
    ) -> None:
        self.b2btenantReposetry = b2btenantReposetry  # Ensure variable names match

    def create(self, b2bTenant_body: B2bTenantSchema) -> B2BTenant:
        location_id = b2bTenant_body.location_id
        exist_location  = self.b2btenantReposetry.db.query(Location).filter(Location.id == location_id).first()
        if not exist_location:
            raise HTTPException(status_code=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION, detail= f"Location with ID {location_id} does not exist.")
            
        b2btenant = self.b2btenantReposetry.create(
            B2BTenant(
                name=b2bTenant_body.name,
                ml_name=b2bTenant_body.ml_name,
                location_id=b2bTenant_body.location_id,
                media=b2bTenant_body.media
            )
        )
        return [b2btenant]
    
    def get(self, b2b_id: int ) -> B2BTenant:
        return self.b2btenantReposetry.get(b2b_id=b2b_id)

