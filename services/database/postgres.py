from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from services.utils import EnvironmentVariables, get_env_variable

DB_HOST = get_env_variable(EnvironmentVariables.DB_HOST.value)
DB_PORT = get_env_variable(EnvironmentVariables.DB_PORT.value)
DB_USER = get_env_variable(EnvironmentVariables.DB_USER.value)
DB_PASSWORD = get_env_variable(EnvironmentVariables.DB_PASSWORD.value)
DB_NAME = get_env_variable(EnvironmentVariables.DB_NAME.value)

SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
