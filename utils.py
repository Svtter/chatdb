import os

from sqlmodel import SQLModel, create_engine


def get_engine():
  """create database file if not exists"""

  # allow user to override db_path by setting DB_PATH environment variable
  db_path = os.getenv("DB_PATH", "chat.db")

  if os.path.exists(db_path):
    engine = create_engine(f"sqlite:///{db_path}")
  else:
    engine = create_engine(f"sqlite:///{db_path}")
    SQLModel.metadata.create_all(engine)
  return engine
