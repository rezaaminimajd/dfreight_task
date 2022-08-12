import logging
from sqlalchemy.orm import Session
from services.database import get_db

from . import models


def add_city(step: int, name: str, url: str, db: Session = next(get_db())):
    try:
        db_city = models.City(
            step=step,
            name=name,
            page_url=url
        )
        db.add(db_city)
        db.commit()
        db.refresh(db_city)
    except Exception as e:
        logging.warning(f"{e}")
        db.rollback()


def update_city_content(step: int, name: str, content: str, db: Session = get_db()):
    db.query(models.City).filter(
        models.City.step == step,
        models.City.name == name,
    ).update(
        {models.City.page_content: content}
    )


def get_cities_by_step(step: int, db: Session = get_db()):
    return db.query(models.City).filter(models.City.step == step).all()
