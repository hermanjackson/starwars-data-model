import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()
favorites = Table('favorite', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('people_id', Integer, ForeignKey('people.id')),
    Column('vehicle_id', Integer, ForeignKey('vehicle.id'))
)


class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    favorite_people = relationship("People",
                    secondary=favorites)
    favorite_vehicles = relationship("Vehicles",
                    secondary=favorites)
    


class People(Base):
    __tablename__ = 'peolple'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    height = Column(String(250))
    eyecolor = Column(String(250), nullable=False)
    weight = Column(Integer, ForeignKey('person.id'))
    



    def to_dict(self):
        return {}
class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')