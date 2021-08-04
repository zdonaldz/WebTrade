from datetime import date
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy.sql.functions import user
from sqlalchemy.sql.sqltypes import Boolean, Date, Integer
from starlette.types import Receive


class User(BaseModel):
    full_name: str
    username: str
    password: str
    mobile: str


class showUser(BaseModel):
    full_name: str
    username: str
    mobile: str
    is_admin: bool
    id: int
    #password: str

    class Config():
        orm_mode = True

class updateUser(BaseModel):
    id : int
    full_name: str
    mobile: str

class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class ShowImg(BaseModel):
    id: int
    url: str

    class Config():
        orm_mode = True

# category

class Category(BaseModel):
    name: str


class ShowCategory(BaseModel):
    id: int
    name: str

    class Config():
        orm_mode = True

# rating


class Rating(BaseModel):
    item_id: int
    user_id: int
    description: str
    stars: int

# posts


class Posts(BaseModel):
    user_id: int
    name: str
    category: int
    ward_code: int
    description: str
    images: List = []

# city


class ShowCity(BaseModel):
    code: int
    name: str

    class Config():
        orm_mode = True

# district


class ShowDistrict(BaseModel):
    code: int
    name: str
    id_city: int
    city_owner: ShowCity

    class Config():
        orm_mode = True

# ward


class ShowWard(BaseModel):
    code: int
    name: str
    id_district: int
    district_owner: ShowDistrict

    class Config():
        orm_mode = True

# item


class ProductAll(BaseModel):
    id: int
    name: str
    description: str
    post_date: date
    is_buy: bool
    images: List[ShowImg] = []
    ward_owner: ShowWard

    class Config():
        orm_mode = True

class SentMessage(BaseModel):
    user_id: int
    receive_id: int
    content: str
    date: date
