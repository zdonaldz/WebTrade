from fastapi import APIRouter
from .. import database, schemas, models, crud
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status
from ..repository import user
from typing import List
router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db


@router.post('/')
def create_user(request: schemas.User,db: Session = Depends(get_db)):
    return user.create(request,db)

@router.get('/all',response_model=List[schemas.showUser])
def get_user(db: Session = Depends(get_db)):
    return user.show(db)

@router.get('/{id}', response_model=schemas.showUser)
def get_user_detail(id:int,db: Session = Depends(get_db)):
    return user.show_detail(id,db)

@router.get('/items/{id}', response_model=List[schemas.ProductAll])
def get_user_item(id:int,db: Session = Depends(get_db)):
    return user.show_item(id,db)

@router.post('/update')
def update_name_user(request: schemas.updateUser, db: Session = Depends(get_db)):
    id = request.id
    full_name = request.full_name
    mobile = request.mobile
    try:
        crud.update_user(db, id, full_name, mobile, None)
    except: 
        return {"error when update "}
    return user.show_detail(id, db)

@router.post("/{id}/setadmin={value}")
def update_rank_users(id:int,value: bool, db: Session = Depends(get_db)):
    u = user.show_detail(id, db)
    try:
        crud.update_user(db, id, u.full_name, u.mobile, value)
    except: 
        return {"error when update "}
    return user.show_detail(id, db)

@router.post('/{user_id}/del')
def del_user(user_id:int, db: Session = Depends(get_db)):
    error = False
    try:
        user.delete_user(db, user_id)
    except :
        error = True
    if error:
        return {"False request"}
    else:
        return {"Success request"}
