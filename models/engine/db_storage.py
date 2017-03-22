#!/usr/bin/python3

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from models import *


class DBStorage:
    __engine = None
    __session = None
    classes = [User, Amenity, Place, City, State, Review]

    def init(self):
        __engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                               .format($HBNB_MYSQL_USER, $HBNB_MYSQL_PWD,
                                       $HBNB_MYSQL_HOST, $HBNB_MYSQL_DB))
        if $HBNB_MYSQL_ENV == 'test':
            Base.metadata.drop_all(__engine)

    def all(self, cls=None):
        objects = {}
        if cls == None:
            for cls in classes:
                for object in self.__session.query(cls):
                    objects[object.id] = object
        else:
            for object in self.__session.query(cls):
                object[object.id] = object
        return objects

    def new(self, obj):
        elif type(obj) == 'Amenity':
            __session.add(Amenity(id=obj.id,
                                  created_at=obj.created_at,
                                  updated_at=obj.updated_at,
                                  name=obj.name))
        elif type(obj) == 'City':
            __session.add(City(id=obj.id,
                               created_at=obj.created_at,
                               updated_at=obj.updated_at,
                               name=obj.name,
                               state_id=obj.state_id))
        elif type(obj) == 'Review':
            __session.add(Review(id=obj.id,
                                 created_at=obj.created_at,
                                 updated_at=obj.updated_at,
                                 text=obj.text,
                                 place_id=obj.place_id,
                                 user_id=obj.user_id))
        elif type(obj) == 'State':
            __session.add(State(id=obj.id,
                                created_at=obj.created_at,
                                updated_at=obj.updated_at,
                                name=obj.name,
                                cities=obj.cities))
        elif type(obj) == 'User':
            __session.add(User(id=obj.id,
                               created_at=obj.created_at,
                               updated_at=obj.updated_at,
                               email=obj.email,
                               password=obj.password,
                               first_name=obj.first_name,
                               last_name=obj.last_name,
                               places=obj.places))
        elif type(obj) == 'Place':
            __session.add(Place(id=obj.id,
                                created_at=obj.created_at,
                                updated_at=obj.updated_at,
                                city_id=obj.city_id,
                                user_id=obj.user_id,
                                name=obj.name,
                                description=obj.description,
                                number_rooms=obj.number_rooms,
                                max_guest=obj.max_guest,
                                price_by_night=obj.price_by_night,
                                latitude=obj.latitude,
                                longitude=obj.longitude,
                                amenity=obj.amenity))

    def save(self):
        __session.commit()

    def delete(self, obj=None):
        __session.delete(obj)

    def reload(self):
        Base.metadata.create_all(__engine)
        __session = sessionmaker(bind=__engine)
