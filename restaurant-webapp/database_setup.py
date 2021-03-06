import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class MenuItem(Base):
    __tablename__ = 'menu_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)


engine = create_engine('sqlite:///restaurantmenu.db')
DBSession = sessionmaker(bind=engine)
Base.metadata.bind=engine
session = DBSession

#if session.query(Restaurant).all() == None:
#    import populatemenus




# >>> from sqlalchemy import create_engine
# >>> from sqlalchemy.orm import sessionmaker
# >>> from database_setup import Base, Restaurant,MenuItem
# >>> engine = create_engine('sqlite:///restaurantmenu.db')
# >>> Base.metadata.bind = engine
# >>> DBSession = sessionmaker(bind = engine)
# >>> session = DBSession()
# >>> session.add(Restaurant(name="New Restaurant"))
# >>> session.commit()
# >>> session.query(Restaurant).all()
# [<database_setup.Restaurant object at 0x000002C9E863D978>]
# >>> session.query(MenuItem).all()
