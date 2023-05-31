from fastapi import FastAPI
from routes import bl_route, auth_route, route_login, route_users
from models import insta
from starlette.middleware.cors import CORSMiddleware
from database import engine
from fastapi.staticfiles import StaticFiles

origins = ["*"]

insta.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(auth_route.router, prefix="")
app.include_router(bl_route.router, prefix="/bl")
app.include_router(route_login.router, prefix="/login")
app.include_router(route_users.router, prefix="/user")