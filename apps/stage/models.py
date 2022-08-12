import datetime
from enum import Enum
from sqlalchemy import Column, Integer, DateTime
from services.database import Base
from sqlalchemy.dialects.postgresql import ENUM


class StageStatus(Enum):
    IN_PROGRESS = 'IN_PROGRESS'
    DONE = 'DONE'


class Stage(Base):
    __tablename__ = "stage"

    id = Column(Integer, primary_key=True, index=True)
    step = Column(Integer, unique=True, index=True)
    start_date = Column(DateTime, default=datetime.datetime.utcnow)
    end_date = Column(DateTime)
    stage_status = Column(ENUM(StageStatus), nullable=False, default=StageStatus.IN_PROGRESS.value)
