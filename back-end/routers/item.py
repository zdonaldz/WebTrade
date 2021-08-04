from fastapi import APIRouter
from .. import database, schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status
from ..repository import item
from typing import List

router = APIRouter(
    prefix="/product",
    tags=['product']
)

get_db = database.get_db


@router.get('/',response_model=List[schemas.ProductAll])
def get_all(db: Session = Depends(get_db)):
    return item.all(db)

@router.get('/{id}')
def get_detail(id:int,db: Session = Depends(get_db)):
    return item.getItemData(id,db)

@router.put('/items/stat/{id}')
def update_item(id: int, db: Session = Depends(get_db)):
    return item.update(id,db)