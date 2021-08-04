from datetime import datetime, date
from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException,status
from ..hashing import Hash

def getItemData(id:int,db:Session):
    item = db.query(models.Item).filter(models.Item.id == id).first()

    #users
    user = db.query(models.User).filter(models.User.id == item.user_id).first()
    item.user = user;

    #ratings
    rating =  db.query(models.Rating).filter(models.Rating.item_id == item.id).all()
    item.rating = rating;

    #images
    image =  db.query(models.Img).filter(models.Img.item_id == item.id).all()
    item.image = image

    #categories
    category = db.query(models.Category).filter(models.Category.id == item.category_id).first()
    item.category = category

    #address
    ward = db.query(models.Ward).filter(models.Ward.code == item.ward_code).first()
    district = db.query(models.District).filter(models.District.code == ward.id_district).first()
    city = db.query(models.City).filter(models.City.code == district.id_city).first()

    class Address:
      def __init__(mysillyobject, _ward, _district, _city):
        mysillyobject.ward = _ward
        mysillyobject.district = _district
        mysillyobject.city = _city
    
    address = Address(ward, district, city)
    item.address = address
  
    return item

def all(db : Session):
    items = db.query(models.Item).all()
    return items

def update(id: int, db: Session):
    db.query(models.Item).filter(models.Item.id == id).update({models.Item.is_buy: True}, synchronize_session=False)
    db.commit()
    return "success"