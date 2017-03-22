#!/usr/bin/python3
from os import getenv
from models import *
from sqlalchemy import Column, String, Table
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    if getenv('HBNB_TYPE_STORAGE', None) == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
