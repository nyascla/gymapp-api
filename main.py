from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.cors import CORSMiddleware

from src.routes import exercise
from src.routes import auth

from src.sqlite import models
from src.sqlite.database import engine, triggers, inserts

models.Base.metadata.create_all(bind=engine)
triggers(engine)
inserts(engine)

app = FastAPI()
app.include_router(exercise.router)
app.include_router(auth.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las fuentes (puedes restringir esto más adelante)
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los headers
)

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")



@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


