from typing import Union

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# root
@app.get("/")
async def serve_spa(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# plantilla entreno
@app.get("/api/workout")
def read_root():
    return {
        "pb": {
            "s": 1,
            "r": 1,
            "p": 1
        },
        "rB": {
            "s": 2,
            "r": 2,
            "p": 2
        },
        "jalon": {
            "s": 3,
            "r": 3,
            "p": 3
        }
    }

# plantilla comida
@app.get("/api/foot")
def read_root():
    return {
        "Comida": "World",
        "Gym": "World",
        "Otros": "World"
    }
# plantilla medidas
@app.get("/api/size")
def read_root():
    return {
        "Comida": "World",
        "Gym": "World",
        "Otros": "World"
    }

@app.get("/api/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# DEV
# uvicorn main:app --reload