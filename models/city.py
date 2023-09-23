#!/usr/bin/python3
""" City Module for HBNB project """
import models
from sqlalchemy import Column, String, Foreignkey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = Colmun(String(60), Foreignkey('states.id'), nullable=False)
    name = Colmun(String(128), nullable=False)
    places = relationship('Place', cascade='all, delete', bachref='cities')
