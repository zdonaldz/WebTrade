from sqlalchemy.orm import Session
from .. import models

def allward(db : Session):
    ward = db.query(models.Ward).all()
    return ward

def alldistrict(db: Session):
    district = db.query(models.District).all()
    return district

def allcity(db: Session):
    city = db.query(models.City).all()
    return city

