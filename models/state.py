#!/usr/bin/python3
from os import getenv
from models import *
from sqlalchemy import Column, String, Table
from sqlalchemy.orm import relationship, backref
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    if getenv('HBNB_TYPE_STORAGE', None) == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state')
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        super(State, self).__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE', None) != 'db':
        @property
        def cities(self):
            city_list = []
            cities = self.storage.all()
            for city in cities.values():
                if isinstance(city, City):
                    if city.state_id == self.id:
                        city_list += city
            return city_list
