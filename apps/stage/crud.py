from datetime import datetime
from sqlalchemy import desc
from sqlalchemy.orm import Session
from services.database import get_db

from . import models


def add_stage(step: int, db: Session = get_db()):
    db_stage = models.Stage(
        step=step,
        start_date=datetime.now()
    )
    db.add(db_stage)
    db.commit()
    db.refresh(db_stage)
    return db_stage


def last_stage(db: Session = get_db()):
    return db.query(models.Stage).order_by(desc(models.Stage.step)).first()


def update_end_date(step: int, db: Session = get_db()):
    db.query(models.Stage).filter(models.Stage.step == step).update(
        {models.Stage.end_date: datetime.now()}
    )
