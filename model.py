from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, Boolean, FLOAT, ForeignKey

BASE = declarative_base()

class ZooComplex(BASE):
    __name__ = 'zoocomplex'
    _id = Column(Integer, primary_key=True, autoincrement=True)
    complex_name = (String(32))
    count = Column(Integer, nullable=True)


class Accommodations(BASE):
    __name__ = 'accommodations'
    _id = Column(Integer, primary_key=True, autoincrement=True)
    complex_id = Column(Integer, ForeignKey(ZooComplex._id), nullable=False)
    has_pool = Column(Boolean)
    area = Column(FLOAT)


class Species(BASE):
    __name__ = 'species'
    _id = Column(Integer, primary_key=True, autoincrement=True)
    accommodation_id = Column(Integer, ForeignKey(Accommodations._id), nullable=False)
    specie_name = Column(String(32))
    family = Column(String(32))
    habitat = Column(String(32))
    live_duration = Column(Integer)

