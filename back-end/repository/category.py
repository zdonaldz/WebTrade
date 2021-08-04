from sqlalchemy.orm import Session
from .. import models, schemas

def allcategory(db : Session):
    category = db.query(models.Category).all()
    return category

def create(request: schemas.Category, db: Session):
    existed = db.query(models.Category).filter(models.Category.name == request.name).first()
    if not existed:
        new_category = models.Category(name=request.name)
        db.add(new_category)
        db.commit()
        db.refresh(new_category)
        return new_category
    else:
        return "category existed"