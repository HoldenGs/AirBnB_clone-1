#!/usr/bin/python3
from models import *
from sqlalchemy import Column, String, orm.relationship
from models.base_model import Base


class State(BaseModel, Base):
    __tablename = 'states'
    name = Column(String(128), nullable=False)
    cities = orm.relationship('City', back_populates='state')

    def __init__(self, *args, **kwargs):
        super(State, self).__init__(*args, **kwargs)
