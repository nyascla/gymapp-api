from fastapi import Depends, FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .dependencies import get_query_token
from .routers import items, users
from .sql_app import models
from .sql_app.database import engine

models.Base.metadata.create_all(bind=engine)

# FastAPI specific code
app = FastAPI(dependencies=[Depends(get_query_token)])
app.include_router(users.router)
app.include_router(items.router)
# COMPILADO
# app.mount("./dist/static", StaticFiles(directory="./dist/static"), name="static")
# templates = Jinja2Templates(directory="./dist/templates")
# ROOT
#@app.get("/")
#async def root(request: Request):
#    return templates.TemplateResponse("./dist/index.html", {"request": request})



# DEV
# uvicorn src.main:app --reload