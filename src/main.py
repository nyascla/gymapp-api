from fastapi import Depends, FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .dependencies import get_query_token
from .routers import etapas, items
from .sql_app import models
from .sql_app.database import engine

models.Base.metadata.create_all(bind=engine)

# FastAPI specific code
# dependencies=[Depends(get_query_token)]
app = FastAPI()
app.include_router(etapas.router)
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
# uvicorn src.main:app --host 192.168.1.133 --port 9876