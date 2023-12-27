from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, Boolean, FLOAT, ForeignKey

BASE = declarative_base()

class ZooComplex(BASE):
    __tablename__ = 'zoocomplex'
    _id = Column(Integer, primary_key=True, autoincrement=True)
    complex_name = Column(String(32), nullable=False)

class Accommodations(BASE):
    __tablename__ = 'accommodations'
    _id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    complex_id = Column(Integer, ForeignKey(ZooComplex._id), nullable=False)
    has_pool = Column(Boolean)
    area = Column(FLOAT)


class Species(BASE):
    __tablename__ = 'species'
    _id = Column(Integer, primary_key=True, autoincrement=True)
    accommodation_id = Column(Integer, ForeignKey(Accommodations._id), nullable=False)
    specie_name = Column(String(32))
    family = Column(String(32))
    habitat = Column(String(32))
    live_duration = Column(Integer)

