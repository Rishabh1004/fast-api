from typing import List, Optional

from fastapi import Depends, HTTPException, status
from models.QomplntModel import Location
from reposetories.LocationRepositry import LocationRepositry
from schemas.QomplntSchema import LocationSchema


class LocationService:
    locationReposetry: LocationRepositry

    def __init__(
            self, locationReposetry: LocationRepositry = Depends()
    ) -> None:
        self.locationReposetry = locationReposetry  # Ensure variable names match

    def create(self, location_data: LocationSchema) -> Location:
        location = self.locationReposetry.create(
             Location(
                geo_id=location_data.geo_id,
                address1=location_data.address1,
                address2=location_data.address2,
                landmark=location_data.landmark,
                city_id=location_data.city_id,
                zip_code=location_data.zip_code
            )
        )
        return [location]

