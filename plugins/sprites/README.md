# Sprites

Use Sprites from Cursor to create, inspect, and operate remote development environments.

Sprites are isolated cloud environments with their own filesystem, URL, services, checkpoints, and network policy. This plugin connects Cursor to the [Fly MCP server](https://mcp.fly.io/guide.md), which serves the Sprites tools, so Cursor can manage those remote environments without treating your local shell as the sprite runtime.

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
- Permission to authenticate Cursor with the Fly MCP server (OAuth, handled in-app on first use). If you used an earlier version of this plugin, which connected to `https://sprites.dev/mcp`, you must authorize once more after updating: the two endpoints have separate OAuth grants.

## What's inside

- **MCP server** (`mcp.json`) — connects Cursor to `https://mcp.fly.io` (remote, OAuth-authenticated) under the server name `sprites`. Depending on what you grant at consent, the server can also expose other Fly.io tools.
- **Skill** (`skills/sprites`) — workflow and safety guidance for operating sprites from Cursor.

## Usage attribution

This plugin tags its requests to the Fly MCP server as coming from Cursor, using the coarse, privacy-safe [`client-signals`](https://github.com/superfly/client-signals) headers. Two fixed values are sent — `cursor` as the client name, and a flag marking the request as non-terminal — so Fly.io can estimate how much Sprites traffic comes through Cursor.

Nothing user-, machine-, or repository-specific is sent, the values never vary between installs, and the tag is advisory analytics only: it is never used for authentication, authorization, access control, gating, or rate-limiting.

## Learn more

- Sprites: https://sprites.dev
- Docs: https://docs.sprites.dev
- Fly MCP guide: https://mcp.fly.io/guide.md
