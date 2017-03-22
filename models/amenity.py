#!/usr/bin/python3
from models import *
from sqlalchemy import Column, String
from models.base_model import Base


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    name = Column(String, nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
