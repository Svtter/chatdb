import os

from sqlmodel import SQLModel, create_engine


def get_engine(db_path: str = "chat.db"):
  """create database file if not exists"""
  if os.path.exists(db_path):
    engine = create_engine(f"sqlite:///{db_path}")
  else:
    engine = create_engine(f"sqlite:///{db_path}")
    SQLModel.metadata.create_all(engine)
  return engine
