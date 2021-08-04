from . import models
from sqlalchemy.orm import Session
from sqlalchemy import or_, and_
import datetime

#------------------------------------------------------
#----------------GET METHOD ---------------------------
#------------------------------------------------------

def get_all_user(db:Session):
    return db.query(models.User)


def get_all_rate(db:Session, item_id):
    return db.query(models.Rating).filter(models.Rating.item_id == item_id).all()

def get_all_chat(db:Session, id_user):
    return db.query(models.Messeage).filter(or_(models.Messeage.user_1 == id_user, models.Messeage.user_2 == id_user)
                                    ).distinct(models.Messeage.user_1, models.Messeage.user_2).all()

def get_mess_room(db:Session, user_1, user_2):
    return db.query(models.Messeage).filter(or_(models.Messeage.user_1 == user_1, models.Messeage.user_2 == user_1)
                                ).filter(or_(models.Messeage.user_1 == user_2, models.Messeage.user_2 == user_2)).order_by(models.Messeage.id).all() 
#------------------------------------------------------
#----------------INSERT METHOD ---------------------------
#------------------------------------------------------

def insert_rating(db:Session, item_id, user_id, content, stars):
    new_rating = models.Rating(user_id=user_id, item_id=item_id, 
                            content=content, stars=stars)
    db.add(new_rating)
    db.commit()
    return get_all_rate(db, item_id)


def insert_item(db:Session, user_id, name, description, category, ward_code):
    is_buy = False
    post_date = datetime.datetime.now()
    #post_date = post_date.year() + "-" + post_date.month() + "-" + post_date.day() 
    
    new_item = models.Item(user_id=user_id, name=name, description=description,
                        category_id=category, ward_code=ward_code, 
                        is_buy=is_buy, post_date=post_date)
    db.add(new_item)
    db.commit()

    return new_item

def insert_img(db:Session, item_id, url):
    new_img = models.Img(item_id=item_id, url=url)
    db.add(new_img)
    db.commit()

def insert_mess(db:Session, user_1, user_2, date, description):
    new_mess = models.Messeage(user_1=user_1, user_2=user_2, date=date, description=description)
    db.add(new_mess)
    db.commit()
    return get_mess_room(db, user_1, user_2)
#------------------------------------------------------
#----------------DELETE METHOD ---------------------------
#------------------------------------------------------

def delete_item(db:Session, item_id):
    db.query(models.Item).filter(models.Item.id == item_id).delete()
    db.commit()
    return


#------------------------------------------------------
#----------------update METHOD ---------------------------
#------------------------------------------------------
def update_user(db:Session, id, full_name, mobile, is_admin):
    info = {"full_name":full_name, "mobile":mobile, "is_admin":is_admin}
    info = {key:info[key] for key in info if not info[key] is None}

    db.query(models.User).filter(models.User.id == id).update(info)
    db.commit()
    return


#___________________________________________________________________________________
