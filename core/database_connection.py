from core.data_connection import user, password, server, port, database
from sqlalchemy import create_engine, pool
from sqlalchemy.orm import sessionmaker, declarative_base
import os


DATABASE_URL = os.getenv("DATABASE_URL")



engine = create_engine(
        DATABASE_URL,
        pool_pre_ping=True,
        connect_args={
            "sslmode": "require"
        }
)

sessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
#sesion = sessionLocal()