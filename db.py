from sqlmodel import Session

from utils import get_engine

engine = get_engine()


def get_session():
  return Session(engine)
