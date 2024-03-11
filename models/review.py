#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """
    A Review representation
    Attributes:
        place_id: represents place id
        user_id: represents user id
        text: represents the text of the review
    """

    place_id = ""
    user_id = ""
    text = ""
