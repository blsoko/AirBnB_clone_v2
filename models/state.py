#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='states')

    if getenv('HBNB_TYPE_STORAGE') != "db":
        @property
        def cities(self):
            """cities"""
            from models.city import City
            from models import storage
            import models
            cityList = []
            for key, value in models.storage.all(City).items():
                if value.state_id == self.id:
                        cityList.append(value)
            return cityList
