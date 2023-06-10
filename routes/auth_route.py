# from apis.version1.route_login import login_for_access_token
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from starlette.responses import HTMLResponse

from database import get_db
from forms.login_form import LoginForm
from routes.route_login import login_for_access_token

templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False, tags=["Auth Activity"])


@router.get("/login/")
def login(request: Request):
    return templates.TemplateResponse("auth/login.html", {"request": request})


@router.post("/login/")
async def login(request: Request, db: Session = Depends(get_db)):
    form = LoginForm(request)
    await form.load_data()
    if await form.is_valid():
        try:
            form.__dict__.update(msg="Login Successful :)")
            response = templates.TemplateResponse("auth/login.html", form.__dict__)
            login_for_access_token(response=response, form_data=form, db=db)
            return response
        except HTTPException:
            form.__dict__.update(msg="")
            form.__dict__.get("errors").append("Incorrect Email or Password")
            return templates.TemplateResponse("auth/login.html", form.__dict__)
    return templates.TemplateResponse("auth/login.html", form.__dict__)


# @router.get("/")
# async def main(request: Request):
#     return templates.TemplateResponse("waiting.html", {"request": request})

@router.get("/")
async def index(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

#
# async def main(request: Request):
#     locations = ["Rome", "Milan", "Florence", "Venice", "Naples", "Bologna", "Pisa", "Siena", "Palermo", "Verona",
#                  "Turin", "Genoa", "Bari", "Catania", "Madrid", "Barcelona"]
#     return templates.TemplateResponse("index.html", {"request": request, 'locations': locations})


@router.get("/map")
async def index(request: Request):
    return templates.TemplateResponse("map.html", {"request": request})


@router.get("/available-lockers")
async def available_lockers(request: Request):
    return {"data": [(33.634283, 73.054358), (33.640320, 73.063402), (33.654302, 73.081956)]}
