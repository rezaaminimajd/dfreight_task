from sqlalchemy import Column, Integer, Text, String, ForeignKey, DateTime, UniqueConstraint
from services.database import Base


class City(Base):
    __tablename__ = "cities"

    __table_args__ = (
        UniqueConstraint("step", "name"),
    )
    id = Column(Integer, primary_key=True, index=True)
    step = Column(Integer)
    name = Column(String, nullable=False)
    page_url = Column(Text, nullable=False)
    page_content = Column(Text)


class OldCity(Base):
    __tablename__ = "old_cities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    city_id = Column(Integer, ForeignKey('cities.id'))
