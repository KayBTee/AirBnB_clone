#!/usr/bin/python3
<<<<<<< HEAD

from models.base_model import BaseModel

class Place(BaseModel):
=======
from models.base_model import BaseModel


class Place(BaseModel):
    """ DOC DOC DOC """
>>>>>>> 8a6d64e364b2ae701f18ba579be1ea361ae99a32
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
<<<<<<< HEAD
    latitutde = 0.0
    longitude = 0.0
    amenity_id = []

=======
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []


""" def __init__(self, city_id, user_id):
    Place.city_id = city_id
    Place.user_id = user_id """
>>>>>>> 8a6d64e364b2ae701f18ba579be1ea361ae99a32
