from fastapi import APIRouter
from .. import database, schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status
from ..repository import address
from typing import List

router = APIRouter(
    prefix="/address",
    tags=['address']
)

get_db = database.get_db

@router.get('/ward',response_model=List[schemas.ShowWard])
def get_ward(db: Session = Depends(get_db)):
    return address.allward(db)

@router.get('/district',response_model=List[schemas.ShowDistrict])
def get_district(db: Session = Depends(get_db)):
    return address.alldistrict(db)

@router.get('/city',response_model=List[schemas.ShowCity])
def get_city(db: Session = Depends(get_db)):
    return address.allcity(db)
    

