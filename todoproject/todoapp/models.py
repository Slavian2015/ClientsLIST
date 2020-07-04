from django.db import models

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Clients(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    city = Column(String(100))
    age = Column(Integer)

    def __init__(self, name, city, age):
        self.name = name
        self.city = city
        self.age = age


    def __str__(self):
        return self.name, self.city, self.age