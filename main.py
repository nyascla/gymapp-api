from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.routes import exercise
from src.routes import auth

from src.sqlite import models
from src.sqlite.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(exercise.router)
app.include_router(auth.router)

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")



@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

