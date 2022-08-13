from sqlalchemy import Column, Integer, Text, String, ForeignKey, DateTime, UniqueConstraint
from services.database import Base


class City(Base):
    __tablename__ = "cities"

    name = Column(String, primary_key=True, nullable=False)
    page_url = Column(Text, nullable=False)
    page_content = Column(Text)


class OldCity(Base):
    __tablename__ = "old_cities"

    __table_args__ = (
        UniqueConstraint("name", "city_name"),
    )

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    city_name = Column(String, ForeignKey('cities.name'))
