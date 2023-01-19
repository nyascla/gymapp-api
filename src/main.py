from fastapi import Depends, FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .dependencies import get_query_token
from .routers import exercises, sessions
from .sql_app import models
from .sql_app.database import engine

models.Base.metadata.create_all(bind=engine)

# FastAPI specific code
# dependencies=[Depends(get_query_token)]
app = FastAPI()
app.include_router(sessions.router)
app.include_router(exercises.router)

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root(request: Request):
   return templates.TemplateResponse("index.html", {"request": request})



# DEV
# uvicorn src.main:app --reload
# uvicorn src.main:app --host 192.168.1.133 --port 9876
