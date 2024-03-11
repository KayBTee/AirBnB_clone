#!/usr/bin/python3

from models.base_model import BaseModel

""" Defines the Place class """


class Place(BaseModel):
    """ Creates the Place model """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitutde = 0.0
    longitude = 0.0
    amenity_id = []
