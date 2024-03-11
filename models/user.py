#!/usr/bin/python3
"""
Definition for
the User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Representation of A User
        email: user's email.
        password: user's password
        first_name: user's first name
        last_name: user's last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
