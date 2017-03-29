#!/usr/bin/python3
from models.user import User
from models.amenity import Amenity
from models.place import PlaceAmenity
from models.place import Place
from models.city import City
from models.state import State
from models.review import Review

from os import environ, getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session
from models.base_model import Base


class DBStorage:
    __engine = None
    __session = None
    classes = {'User': User, 'Amenity': Amenity, 'Place': Place,
               'City': City, 'State': State, 'Review': Review}

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(environ['HBNB_MYSQL_USER'],
                                              environ['HBNB_MYSQL_PWD'],
                                              environ['HBNB_MYSQL_HOST'],
                                              environ['HBNB_MYSQL_DB']))
        if getenv('HBNB_MYSQL_ENV', None) == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        objects = {}
        if cls:
            for object in self.__session.query(cls).all():
                objects[object.id] = object
        else:
            for cls in self.classes:
                cls = self.classes[cls]
                for object in self.__session.query(cls).all():
                    objects[object.id] = object
        return objects

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        self.__session.delete(obj)

    def close(self):
        self.__session.remove()

    def reload(self):
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine))
