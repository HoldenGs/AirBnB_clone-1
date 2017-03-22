#!/usr/bin/python3
from models import *
from sqlalchemy import Column, String, orm.relationship
from models.base_model import Base


class User(BaseModel, Base):
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    places = orm.relationship('Place', back_populates='user')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
