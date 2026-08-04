from __future__ import annotations

import json
import unittest
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


class CursorPluginRepositoryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.marketplace = load_json(ROOT / ".cursor-plugin/marketplace.json")
        self.listing = self.marketplace["plugins"][0]
        self.plugin_root = ROOT / self.listing["source"]
        self.manifest = load_json(self.plugin_root / ".cursor-plugin/plugin.json")

    def test_marketplace_points_to_plugin(self) -> None:
        self.assertEqual(self.marketplace["name"], self.manifest["name"])
        self.assertEqual(self.listing["name"], self.manifest["name"])
        self.assertTrue(self.plugin_root.is_dir())

    def test_manifest_references_existing_assets(self) -> None:
        self.assertTrue((self.plugin_root / self.manifest["logo"]).is_file())
        self.assertTrue((self.plugin_root / "skills/sprites/SKILL.md").is_file())

    def test_manifest_repository_matches_this_repository(self) -> None:
        self.assertEqual(
            self.manifest["repository"],
            "https://github.com/superfly/sprites-cursor-plugin",
        )

    def test_mcp_server_uses_https(self) -> None:
        config = load_json(self.plugin_root / "mcp.json")
        server = config["mcpServers"]["sprites"]
        parsed = urlparse(server["url"])
        self.assertEqual(parsed.scheme, "https")
        self.assertEqual(parsed.netloc, "sprites.dev")
        self.assertEqual(parsed.path, "/mcp")


if __name__ == "__main__":
    unittest.main()
