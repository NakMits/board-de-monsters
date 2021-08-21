import os
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from cmn.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/cards/", response_model=List[schemas.Card])
def get_cards(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cards = crud.read_cards(db, skip=skip, limit=limit)
    return cards


@app.get("/cards/{name}", response_model=schemas.Card)
def get_card(name: str, db: Session = Depends(get_db)):
    card = crud.read_card_by_name(db, name=name)
    if card is None:
        raise HTTPException(status_code=404, detail="Card not found")
    return card


@app.get("/skills/", response_model=List[schemas.Skill])
def get_skills(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    skills = crud.read_skills(db, skip=skip, limit=limit)
    return skills


@app.get("/skills/{name}", response_model=schemas.Skill)
def get_skill(name: str, db: Session = Depends(get_db)):
    skill = crud.read_skill_by_name(db, name=name)
    if skill is None:
        raise HTTPException(status_code=404, detail="Skill not found")
    return skill


# ローカル開発用
if __name__ == '__main__':
    import uvicorn as uvicorn

    uvicorn.run(app="main:app", reload=True)
# port=int(os.environ.get(ENVIRON.PORT.value)),
