#!/usr/bin/python3
from models import *
from sqlalchemy import Column, String, ForeignKey
from models.base_model import Base


class City(BaseModel, Base):
    __tablename__ = 'cities'
    state_id = Column(String(60), nullable=False)
    name = Column(String(128), nullable=False, ForeignKey('states.id'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
