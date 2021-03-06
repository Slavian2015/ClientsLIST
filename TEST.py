from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sqlalchemy



Base = declarative_base()

class Student(Base):

    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    city = Column(String(100))
    age = Column(Integer)

    def __init__(self, name, city, age):
        self.name = name
        self.city = city
        self.age = age

    def __repr__(self):
        return self.name, self.city, self.age


connection_setup = "mysql://root:s1n1s1n1@localhost:3306/mysql"

engine = sqlalchemy.create_engine(connection_setup)

Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)