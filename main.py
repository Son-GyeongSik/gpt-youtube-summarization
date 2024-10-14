from fastapi.templating import Jinja2Templates

from script import *
from summary import *
from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
import uvicorn
import crud
from model import Base, Summary
from database import SessionLocal, engine
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

templates = Jinja2Templates(directory="templates")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/summary")
async def summary(request: Request, db: Session = Depends(get_db), code: str = ""):

    summary_schema = crud.db_get_summary(db, code)

    if summary_schema:
        return summary_schema.summary

    summary = await root(code)
    crud.db_add_summary(db, summary, code)
    return summary


async def root(code: str, summary_mode: int = 1, mode: int = 3):

    script = Script()
    get_script(script, code)

    if summary_mode == 1:
        summary = await generate_summary(script.text, mode)

    elif summary_mode == 2:
        summary = await generate_compress_summary(script.text, mode)

    return summary

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=80)