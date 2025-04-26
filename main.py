from select import select

from fastmcp import MCP

from db import get_session


def get_mcp():
  return MCP(
    host="localhost",
    port=8080,
    username="admin",
    password="admin",
  )


mcp = get_mcp()


@mcp.tool()
def record(system: str, user: str, tags: str):
  """当你想要记录对话的时候，可以调用这个工具
  system: 对话的系统
  user: 对话的用户
  tags: 对话的标签
  """
  from schema import Record

  record = Record(system=system, user=user, tags=tags)
  with get_session() as session:
    session.add(record)
    session.commit()
  return f"已记录对话: {system} {user} {tags}"


@mcp.tool()
def read(tags: str):
  """当你想要读取对话的时候，可以调用这个工具
  tags: 对话的标签
  """
  from schema import Record

  with get_session() as session:
    records = session.exec(select(Record).where(Record.tags == tags)).all()
    return records


if __name__ == "__main__":
  mcp.run()
