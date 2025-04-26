from functools import cache

from fastmcp import FastMCP

from chatdb import chatdb


def get_mcp():
  return FastMCP(
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
  chatdb.insert_chat(system, user, tags)
  return {"result": f"已记录对话: {system} {user} {tags}"}


@mcp.tool()
def read(tags: str):
  """当你想要读取对话的时候，可以调用这个工具
  tags: 对话的标签
  """
  return {"record": chatdb.get_chat(tags)}


if __name__ == "__main__":
  mcp.run()
