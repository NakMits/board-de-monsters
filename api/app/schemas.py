from pydantic import BaseModel


class CardBase(BaseModel):
    pass


class Card(CardBase):
    name: str
    type: str
    text: str
    skill: str
    hp: int
    pw: int
    df: int
    ap: int
    after_evo: str
    before_evo: str

    class Config:
        orm_mode = True


class SkillBase(BaseModel):
    pass


class Skill(SkillBase):
    name: str
    mp: int
    range: str
    text: str

    class Config:
        orm_mode = True
