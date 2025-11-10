from __future__ import annotations

import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from agents.utils.manifest import ManifestHandler


class ManifestHandlerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp_dir = TemporaryDirectory()
        self.base = Path(self.tmp_dir.name) / "drive" / "Context" / "_pipeline"
        self.handler = ManifestHandler(self.base)

    def tearDown(self) -> None:
        self.tmp_dir.cleanup()

    def test_write_and_read_manifest(self) -> None:
        payload = {"process": "00-Test", "status": "completed"}
        path = self.handler.write("00-Test-manifest.json", payload)
        self.assertTrue(path.exists())

        loaded = self.handler.read("00-Test-manifest.json")
        self.assertEqual(loaded, payload)

    def test_list_manifests_returns_sorted_entries(self) -> None:
        self.handler.write("b-manifest.json", {"status": "draft"})
        self.handler.write("a-manifest.json", {"status": "done"})
        self.assertEqual(
            self.handler.list_manifests(),
            ["a-manifest.json", "b-manifest.json"],
        )


if __name__ == "__main__":
    unittest.main()
