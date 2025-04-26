# ChatDB

This is an MCP server that records all your conversations with Cursor.

A easier memory layer for gpt.

## Install

```bash
uv sync
```

## Usage

Config this to MCP server.


```json
{
  "mcpServers": {
    "chatdb": {
      "commands": "",
      "env": {
        "env": "<your-database-path>"
      }
    }
  }
}
```

## LICENSE

AGPL