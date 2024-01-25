from typing import List, Optional

from fastapi import Depends, HTTPException, status
from models.QomplntModel import City
from reposetories.CityRepositry import CityRepositry
from schemas.QomplntSchema import CitySchema


class CityService:
    cityReposetry: CityRepositry

    def __init__(
            self, cityReposetry: CityRepositry = Depends()
    ) -> None:
        self.cityReposetry = cityReposetry # Ensure variable names match

    def create(self, city_body: CitySchema) -> City:
        city =  self.cityReposetry.create(
            City(
                city = city_body.city,
                district = city_body.district,
                state = city_body.state,
                country = city_body.country
            )
        )
        return [city]
    

