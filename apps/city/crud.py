import logging
from sqlalchemy.orm import Session
from services.database import get_db

from . import models


def upsert_city(name: str, url: str, db: Session = next(get_db())):
    try:
        result = db.query(models.City).filter(models.City.name == name).first()
        if result:
            db.query(models.City).filter(models.City.name == name).update(
                {models.City.page_url: url}
            )
        else:
            db_city = models.City(
                name=name,
                page_url=url
            )
            db.add(db_city)
        db.commit()
    except Exception as e:
        logging.warning(f"{e}")
        db.rollback()


def update_city_content(name: str, content: str, db: Session = get_db()):
    db.query(models.City).filter(
        models.City.name == name,
    ).update(
        {models.City.page_content: content}
    )


def add_old_city(old: str, new: str, db: Session = next(get_db())):
    try:
        result = db.query(models.OldCity).filter(
            models.OldCity.city_name == new,
            models.OldCity.name == old
        ).first()
        if not result:
            db_city = models.OldCity(
                name=old,
                city_name=new
            )
            db.add(db_city)
            db.commit()
            db.refresh(db_city)
    except Exception as e:
        logging.error(e)
        db.rollback()

