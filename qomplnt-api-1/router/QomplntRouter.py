from typing import List, Optional, Dict
from fastapi import APIRouter, status, Depends, HTTPException
from schemas.QomplntSchema import (QomplantQrSchema,
                                    B2bTenantSchema,
                                      LocationSchema,
                                        MultiLingualTextSchema,
                                        CitySchema,
                                          QomplantQrLocationSchema, 
                                          B2bTenantLocationSchema,
                                          DMLResponce)
from services.QomplantQrService import QomplantQrService
from services.B2BTenantService import B2BTenantService
from services.LocationService import LocationService
from services.MLTextService import MLTextService
from services.CityService import CityService
from models.QomplntModel import QomplntQr
from middleware.auth_middleware import check_token


QomplntRouter =APIRouter(
    prefix='/qomplnt',
    tags=['qomplnt']  
)


# post
@QomplntRouter.post(
    '/qomplntqr',
    response_model= List[DMLResponce],

    status_code=status.HTTP_201_CREATED
)
def create(
    qomplnor: QomplantQrSchema,
    qomplntQrService: QomplantQrService = Depends(),
):
    return qomplntQrService.create(qomplnor)
# get
@QomplntRouter.get('/qomplntqr', response_model=List[QomplantQrLocationSchema])
def get_qomplntqr(lang_code: int, uuid: str, qomplantQrService: QomplantQrService = Depends()):
    qomplnt_data = qomplantQrService.get(lang_code, uuid)
    return qomplnt_data
   


# B2bTenant
@QomplntRouter.post(
    '/b2btenant',
    response_model= List[DMLResponce],
    status_code=status.HTTP_201_CREATED
)
def create_b2btenant(
    b2btenant: B2bTenantSchema,  # Use b2btenant as the request body
    b2bTenantService: B2BTenantService = Depends()
):
    return b2bTenantService.create(b2btenant)

@QomplntRouter.get('/b2btenant', response_model=List[B2bTenantLocationSchema])
def get_b2btenant(id: int, b2bTenantService: B2BTenantService = Depends()):
    b2btenant_data = b2bTenantService.get(id)
    return b2btenant_data


# Location 
@QomplntRouter.post(
    '/location',
    response_model= List[DMLResponce],
    status_code= status.HTTP_201_CREATED
)
def create_location(
    location:LocationSchema,
    locationService: LocationService = Depends()
):
    return locationService.create(location)

# Multi Lingual Text
@QomplntRouter.post(
    '/mltext',
    response_model= List[DMLResponce]
)
def create_mltext(
    mltext:MultiLingualTextSchema,
    mltextServive:MLTextService = Depends() 
):
    return mltextServive.create(mltext)
    



# City 
@QomplntRouter.post(
    '/city',
    # response_model=List[Dict[str, str]]
    response_model= List[DMLResponce]
    # response_model=List[CitySchema]
)
def create_city(
    city : CitySchema,
    cityService : CityService = Depends() 
):
    return cityService.create(city)


# QomplntRouter.add_middleware(check_token)# Applying the middleware to the router
