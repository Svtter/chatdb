from datetime import datetime

from sqlmodel import Field, SQLModel


class Record(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  system: str
  user: str
  tags: str
  created_at: datetime = Field(default_factory=datetime.now)
  updated_at: datetime = Field(default_factory=datetime.now)
