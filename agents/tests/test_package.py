from __future__ import annotations

import unittest
import zipfile
from pathlib import Path
from tempfile import TemporaryDirectory

from agents.utils.package import package_artifacts


class PackageArtifactsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp_dir = TemporaryDirectory()
        self.base_path = Path(self.tmp_dir.name)
        self.strategy_dir = self.base_path / "drive" / "Ctx" / "ZeroUm"
        self.strategy_dir.mkdir(parents=True, exist_ok=True)
        (self.strategy_dir / "00-arquivo.MD").write_text("conteudo", encoding="utf-8")

    def tearDown(self) -> None:
        self.tmp_dir.cleanup()

    def test_package_generates_zip_with_contents(self) -> None:
        archive = package_artifacts("Ctx", "ZeroUm", base_path=self.base_path)
        self.assertTrue(archive.exists())
        self.assertEqual(archive.suffix, ".zip")

        with zipfile.ZipFile(archive) as zf:
            self.assertIn("00-arquivo.MD", zf.namelist())

    def test_package_overwrites_existing_zip(self) -> None:
        first = package_artifacts("Ctx", "ZeroUm", base_path=self.base_path)
        previous_mtime = first.stat().st_mtime
        second = package_artifacts("Ctx", "ZeroUm", base_path=self.base_path)
        self.assertGreaterEqual(second.stat().st_mtime, previous_mtime)


if __name__ == "__main__":
    unittest.main()
