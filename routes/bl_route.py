import random
import time

import redis
from fastapi import APIRouter, Depends, HTTPException, Request, Form
from starlette.templating import Jinja2Templates
import crud
from database import get_db
from schemas import schemas
from sqlalchemy.orm import Session
from sse_starlette.sse import EventSourceResponse

templates = Jinja2Templates(directory="templates")
redis_client = redis.Redis(host='127.0.0.1', port=6379, db=0)

router = APIRouter(tags=["Bag Locker Activity"])


@router.post("/find-locker/", description=" User finds nearer locker in response to his location",
             response_model=schemas.BotBase)
def create_bot(bot: schemas.BotBase, db: Session = Depends(get_db)):
    crud.creat_bot(db, bot)
    return {"message": "Bot added successfully"}


async def logGenerator(request):
    while (True):
        if await request.is_disconnected():
            print("client disconnected!!!")
            break
        if redis_client.get("tester"):
            done, total = redis_client.get("tester").decode().split(',')
            progress = round((int(done) / int(total)) * 100, 2)
            yield str(progress)  # str(random.randint(0, 100))
        else:
            yield str(0)
        time.sleep(1)


@router.get('/stream-logs')
async def runStatus(request: Request):
    event_generator = logGenerator(request)
    return EventSourceResponse(event_generator)


@router.get("/notify-user")
async def main(request: Request):
    return {"sattus": "Success", "message": "otp email sent to user"}


@router.get("/verify-payment")
async def main(request: Request):
    return {"sattus": "Success", "message": "waiting for the payment gateway"}


@router.get("/notify-user")
async def main(request: Request):
    return {"sattus": "Success", "message": "otp email sent to user"}


