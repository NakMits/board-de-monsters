from sqlalchemy import Column, Integer, String

from cmn.database import Base


class Card(Base):
    __tablename__ = "card"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    text = Column(String)
    skill = Column(String)
    hp = Column(Integer)
    pw = Column(Integer)
    df = Column(Integer)
    ap = Column(Integer)
    after_evo = Column(String)
    before_evo = Column(String)


class Skill(Base):
    __tablename__ = "skill"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    mp = Column(Integer)
    range = Column(String)
    text = Column(String)
