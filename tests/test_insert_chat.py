from chatdb import chatdb


def test_insert_chat():
  chatdb.insert_chat("system", "user", "tags")
  assert len(chatdb.get_chat("tags")) > 0
