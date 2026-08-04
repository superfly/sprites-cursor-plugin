# Sprites for Cursor

The official [Cursor](https://cursor.com) plugin for [**Sprites**](https://sprites.dev) — sandboxed, checkpointable remote development environments you can create, run commands in, and manage services on, all from Cursor's agent.

This repository is a Cursor Marketplace plugin. It bundles the hosted **Sprites MCP server** plus a skill that guides the agent through common sprite workflows. There is no server code here — the MCP server is operated by [Fly.io](https://fly.io) and reached remotely at `https://sprites.dev/mcp` over OAuth-authenticated HTTPS.

## Install

- **Marketplace:** install the **Sprites** plugin from the Cursor Marketplace.
- **From this repo:** point Cursor at this repository / the `plugins/sprites` plugin.

On first use, Cursor prompts you to authorize with Sprites via OAuth.

## Usage attribution

The plugin marks its hosted MCP requests as Cursor-driven using the coarse,
privacy-safe [`client-signals`](https://github.com/superfly/client-signals)
headers. The marker is advisory analytics only and is never used for access
control, gating, or rate-limiting.

## What it provides

- **`plugins/sprites/mcp.json`** — the remote Sprites MCP server (`https://sprites.dev/mcp`).
- **`plugins/sprites/skills/sprites`** — a skill with workflow and safety guidance for operating sprites.

## Repository layout

```
.cursor-plugin/marketplace.json          Marketplace manifest
plugins/sprites/
  .cursor-plugin/plugin.json             Plugin manifest
  mcp.json                               Remote MCP server config
  README.md                              Plugin readme
  assets/sprites-logo.svg                Logo
  skills/sprites/SKILL.md                Sprites workflow skill
```

## Related

- Remote MCP listing: [`dev.sprites/mcp`](https://registry.modelcontextprotocol.io/v0/servers?search=dev.sprites/mcp) in the official MCP registry ([superfly/sprites-mcp](https://github.com/superfly/sprites-mcp))
- Sprites: https://sprites.dev · Docs: https://docs.sprites.dev

## License

[MIT](./LICENSE) © Fly.io, Inc.
