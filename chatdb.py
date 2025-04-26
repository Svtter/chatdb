from sqlmodel import Session, select

from schema import Record
from utils import get_engine


class ChatDB:
  def __init__(self):
    self.engine = get_engine()

  def get_session(self):
    return Session(self.engine)

  def insert_chat(self, system: str, user: str, tags: str):
    with self.get_session() as session:
      session.add(Record(system=system, user=user, tags=tags))
      session.commit()

  def get_chat(self, tags: str):
    with self.get_session() as session:
      records = session.exec(select(Record).where(Record.tags == tags)).all()
      return [record.model_dump() for record in records]


chatdb = ChatDB()
