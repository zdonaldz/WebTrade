from fastapi import FastAPI
from . import  models
from .database import engine
from .routers import user, authentication, item, rating, posts, category, address, meassage
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#CORS
origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(engine)

#router
app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(item.router)
app.include_router(rating.router)
app.include_router(posts.router)
app.include_router(category.router)
app.include_router(address.router)
app.include_router(meassage.router)