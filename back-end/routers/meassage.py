from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database, crud, schemas

router = APIRouter(
    prefix="/messeage",
    tags=['messeage']
)

get_db = database.get_db


@router.post('/')
def send(mess:schemas.SentMessage, db: Session = Depends(get_db)):
    user_id = mess.user_id
    receive_user = mess.receive_id
    date = mess.date
    content = mess.content
    return crud.insert_mess(db, user_id, receive_user, date, content)


@router.get('/room')
def get_room(user_id:int, user_2:int, db: Session = Depends(get_db)):
    mess = crud.get_mess_room(db, user_id, user_2)    
    return mess

@router.get('/allchat/{user_id}')
def get_all_chat(user_id:int, db: Session = Depends(get_db)):
    rooms = crud.get_all_chat(db, user_id)
    rooms = [{'user_1': x.user_1, "user_2":x.user_2} if user_id==x.user_1 
            else {'user_1': x.user_2, "user_2":x.user_1}  for x in rooms]
    rooms = [dict(t) for t in {tuple(d.items()) for d in rooms}]
    return rooms