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

`plugins/sprites/mcp.json` sets two static headers:

| Header | Value | Why |
|---|---|---|
| `Fly-Client-Agent` | `cursor` | The canonical agent tag from [`spec/markers.json`](https://github.com/superfly/client-signals/blob/main/spec/markers.json). Any other spelling would be classified as `other`. |
| `Fly-Client-Interactive` | `false` | Required. See below. |

**Don't remove `Fly-Client-Interactive`, and don't "correct" it to `true`.**
Both are easy mistakes to make, and both are silent:

- It is the *instrumentation sentinel*. Per
  [`spec/request-metrics.md`](https://github.com/superfly/client-signals/blob/main/spec/request-metrics.md),
  a request missing this header — or carrying an unparseable value — classifies
  as `{"operator": "uninstrumented", "agent": "none"}`, and `Fly-Client-Agent`
  is discarded along with it. Dropping this header zeroes out all attribution.
- `false` is correct despite Cursor being human-driven. `Interactive` means
  "stdout looks attached to a terminal," not "a human is present." These
  requests originate from Cursor's MCP client, where no terminal is attached.
  The value is also inert for reporting: operator precedence is
  `ci > agent > interactive`, so a present `Fly-Client-Agent` yields
  `operator="agent"` either way.

`Fly-Client-Parent` and `Fly-Client-CI` are deliberately omitted — the spec
states that `Parent` must not affect classification, and false-valued `CI` is
omitted rather than sent.

To confirm attribution is arriving, check `fly_client_signals_requests_total`
server-side: `operator="agent", agent="cursor"` means the headers landed;
`operator="uninstrumented", agent="none"` means the client stripped them.

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
