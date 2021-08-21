from sqlalchemy.orm import Session

import models


def read_cards(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Card).offset(skip).limit(limit).all()


def read_card_by_name(db: Session, name: str):
    return db.query(models.Card).filter(models.Card.name == name).first()


def read_skills(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Skill).offset(skip).limit(limit).all()


def read_skill_by_name(db: Session, name: str):
    return db.query(models.Skill).filter(models.Skill.name == name).first()
