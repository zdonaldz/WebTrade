from os import name
from fastapi import APIRouter
from .. import database, schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status
from ..repository import category
from typing import List

router = APIRouter(
    prefix="/category",
    tags=['category']
)

get_db = database.get_db

@router.get('/',response_model=List[schemas.ShowCategory])
def get_all_category(db: Session = Depends(get_db)):
    return category.allcategory(db)

@router.post('/')
def create_category(request: schemas.Category,db: Session = Depends(get_db)):
    return category.create(request,db)