#!/usr/bin/python3
"""This is the state class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import shlex
from os import environ


class State(BaseModel, Base):
    """This is the class for State
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if environ['HBNB_TYPE_STORAGE'] == 'db':
        cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")
    else:
        @property
        def cities(self):
            from models import storage
            from models.city import City
            # return list of City objs in __objects
            cities_dict = storage.all(City)
            cities_list = []

            # copy values from dict to list
            for city in cities_dict.values():
                if city.state_id == self.id:
                    cities_list.append(city)

            return cities_list