from fastapi import APIRouter, Depends, File, UploadFile, Form
from sqlalchemy.orm import Session
from .. import database, crud, schemas
import cloudinary
import cloudinary.uploader
import cloudinary.api
from typing import List

router = APIRouter(
    prefix="/posts",
    tags=['posts']
)

get_db = database.get_db
cloudinary.config( 
  cloud_name = "int3306uet", 
  api_key = "748356266443834", 
  api_secret = "B9lB62U3x-Kyqxpfzp5EGGfoHFU" 
)

def up_img_to_cloud(img, img_id):
    url = '/home/tradingweb/items/'+ str(img_id)
    r = cloudinary.uploader.upload(img, folder=url)
    return r['url']

#--------------------POST-------------------------------------------
@router.post('/')
async def create_posts(name:str = Form(...), user_id:int = Form(...), category:int = Form(...),
            description:str = Form(...), ward_code:int = Form(...),
            images: List[UploadFile]= File(...) ,db: Session = Depends(get_db)):
    
    error = False
    try:
        item = crud.insert_item(db, user_id, name, description, category, ward_code)
    except :
        print("error when insert new item")
        error = True

    try:
        for img in images:
            content = img.file
            url = up_img_to_cloud(content, item.id)
            crud.insert_img(db, item.id, url)
    except:
        if not error:
            crud.delete_item(db, item.id)
        error = True
        print("error in upload img upto cloud")

    if error:
        return {"False request"}
    else:
        return {"item_id":item.id}

#-----------------------------------------
@router.post('/{item_id}/del')
def del_posts(item_id:int, db: Session = Depends(get_db)):
    error = False
    try:
        crud.delete_item(db, item_id)
    except :
        error = True
    if error:
        return {"False request"}
    else:
        return {"Success request"}

#------------------ GET ------------------------------------------
