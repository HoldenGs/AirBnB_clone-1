#!/usr/bin/python3
from models import *
from sqlalchemy import Column, String, ForeignKey
from models.base_model import Base


class Review(BaseModel, Base):
    __tablename__ = 'reviews'
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), nullable=False, ForeignKey('places.id'))
    user_id = Column(String(60), nullable=False, Foreign('users.id'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
