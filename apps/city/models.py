from sqlalchemy import Column, Integer, Text, String, ForeignKey, DateTime
from services.database import Base


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    step = Column(Integer)
    name = Column(String, nullable=False)
    page_url = Column(Text, nullable=False)
    page_content = Column(Text)


class OldCity(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    city_id = Column(Integer, ForeignKey('cities.id'))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
