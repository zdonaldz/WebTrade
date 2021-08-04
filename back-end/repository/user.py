from datetime import datetime, date
from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status
from ..hashing import Hash


def create(request: schemas.User, db: Session):
    existed = db.query(models.User).filter(models.User.username == request.username).first()
    if not existed:
        new_user = models.User(full_name=request.full_name, username=request.username, password=Hash.bcrypt(
            request.password), mobile=request.mobile, is_admin=False)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    else:
        return "username existed"


def show(db: Session):
    user = db.query(models.User).all()
    return user


def show_item(id: int, db: Session):
    item = db.query(models.Item).filter(models.Item.user_id == id).all()
    return item

def show_detail(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    return user

def delete_user(db:Session, id):
    db.query(models.User).filter(models.User.id == id).delete()
    db.commit()
    return
        