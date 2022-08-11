from sqlalchemy import desc
from sqlalchemy.orm import Session
from services.database import get_db

from . import models


def add_stage(step: int, db: Session = get_db()):
    db_stage = models.Stage(
        step=step
    )
    db.add(db_stage)
    db.commit()
    db.refresh(db_stage)
    return db_stage


def last_stage(db: Session = get_db()):
    return db.query(models.Stage).order_by(desc(models.Stage.step)).first()
