from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime
from .database import Base

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    username = Column(String, unique=True)
    password = Column(String)
    mobile = Column(String, unique=True)
    is_admin = Column(Boolean)

    items = relationship("Item", back_populates="user_owner")
    ratings = relationship("Rating", back_populates="user_owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    post_date = Column(Date)
    is_buy = Column(Boolean, default=False)

    user_id = Column(Integer, ForeignKey("users.id"))
    user_owner = relationship("User", back_populates="items")
  
    category_id = Column(Integer, ForeignKey("categories.id"))
    category_owner = relationship("Category", back_populates="items")

    #address
    ward_code = Column(Integer, ForeignKey("wards.code"))
    ward_owner = relationship("Ward", back_populates="items")

    ratings = relationship("Rating", back_populates="item_owner")
    images = relationship("Img", back_populates="item_owner")


class Img(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    item_id = Column(Integer, ForeignKey("items.id"))
    item_owner = relationship("Item", back_populates='images')

class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    item_id = Column(Integer, ForeignKey("items.id"))
    content = Column(String)
    stars = Column(Integer)

    user_owner = relationship("User", back_populates="ratings")
    item_owner = relationship("Item", back_populates="ratings")

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    items = relationship("Item", back_populates="category_owner")

class Ward(Base):
    __tablename__ = "wards"

    code = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    id_district = Column(Integer, ForeignKey("districts.code"))
    district_owner = relationship("District", back_populates="wards")

    items = relationship("Item", back_populates="ward_owner")

#-----------------------------------------------------------------
class District(Base):
    __tablename__ = "districts"
    code = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    id_city = Column(Integer, ForeignKey("city.code"))
    city_owner = relationship("City", back_populates="districts")

    wards = relationship("Ward", back_populates="district_owner")

#-----------------------------------------------------------------
class City(Base):
    __tablename__ = "city"
    code = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    districts = relationship("District", back_populates="city_owner")

#------------------------------------------------------------------
class Messeage(Base):
    __tablename__ = "messeages"
    id = Column(Integer, primary_key=True, index=True)
    user_1 = Column(Integer, ForeignKey("users.id"))
    user_2 = Column(Integer, ForeignKey("users.id"))
    date = Column(Date)
    description = Column(String)