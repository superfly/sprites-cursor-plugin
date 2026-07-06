# Sprites

Use Sprites from Cursor to create, inspect, and operate remote development environments.

Sprites are isolated cloud environments with their own filesystem, URL, services, checkpoints, and network policy. This plugin connects Cursor to the [Sprites MCP server](https://sprites.dev/mcp) so Cursor can manage those remote environments without treating your local shell as the sprite runtime.

## What you can do

With this plugin enabled, you can ask Cursor to:

- List your active sprites.
- Create a fresh remote environment for a task.
- Inspect a sprite's files, services, logs, checkpoints, and network policy.
- Run commands, tests, builds, and diagnostics inside a selected sprite.
- Start long-running services such as dev servers, background workers, and databases.
- Create checkpoints before risky changes.
- Clean up services or destroy sprites when you explicitly ask for that.

## Requirements

- Cursor with plugin support.
- Access to Sprites for your organization.
- Permission to authenticate Cursor with the Sprites MCP server (OAuth, handled in-app on first use).

## What's inside

- **MCP server** (`mcp.json`) — connects Cursor to `https://sprites.dev/mcp` (remote, OAuth-authenticated).
- **Skill** (`skills/sprites`) — workflow and safety guidance for operating sprites from Cursor.

## Learn more

- Sprites: https://sprites.dev
- Docs: https://docs.sprites.dev
- Remote MCP: https://docs.sprites.dev/integrations/remote-mcp/
