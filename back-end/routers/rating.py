from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database, crud, schemas

router = APIRouter(
    prefix="/rating",
    tags=['rating']
)

get_db = database.get_db


@router.post('/')
def create_rating(rating:schemas.Rating, db: Session = Depends(get_db)):
    item_id = rating.item_id
    user_id = rating.user_id
    content = rating.description
    stars = rating.stars
    return crud.insert_rating(db, item_id, user_id, content, stars)


@router.get('/{item_id}')
def get_all_rating(item_id:int,  db: Session = Depends(get_db)):
    ratings = crud.get_all_rate(db, item_id)    
    r = [{"id":r.id, "user_id":r.user_id, "content":r.content, "stars":r.stars,
                "user_name": r.user_owner.full_name} for r in ratings]
    return r
