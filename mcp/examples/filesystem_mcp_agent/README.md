# Filesystem MCP agent (skeleton)

Wires an agent to a filesystem MCP server with strict allow-listing.

## Use case
Agent that reads + edits files in a single project root, never escapes.

## Allow-list
The single most important config:

```json
{
  "command": "filesystem-mcp",
  "args": ["--allow", "/workspace/my-project", "--read-only-glob", "**/.env*"]
}
```

- Limit roots to one project
- Mark secret-bearing patterns read-only (or excluded)
- Never grant `/`, `~`, or any home directory

## Risk-tiered tools

| Tool | Risk | Approval |
|---|---|---|
| `read_file` | Low | none |
| `list_dir` | Low | none |
| `write_file` (within allow-list) | Medium | none |
| `delete_file` / `move_file` | High | required |

## Hardening

- Run the server in a container with FS bind-mounts limited to the project root
- Disable network access for the container
- Audit-log every write
