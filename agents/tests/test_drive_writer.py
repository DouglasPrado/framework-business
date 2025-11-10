from __future__ import annotations

import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from agents.utils.drive_writer import next_prefixed_name, write_artifact


class DriveWriterTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp_dir = TemporaryDirectory()
        self.folder = Path(self.tmp_dir.name) / "drive" / "Ctx" / "00-TestProcess"
        self.folder.mkdir(parents=True, exist_ok=True)

    def tearDown(self) -> None:
        self.tmp_dir.cleanup()

    def test_next_prefixed_name_increments_based_on_existing_files(self) -> None:
        first = next_prefixed_name(self.folder, "resumo")
        self.assertTrue(first.name.startswith("01-resumo"))
        first.write_text("conteudo", encoding="utf-8")

        second = next_prefixed_name(self.folder, "diagnostico")
        self.assertTrue(second.name.startswith("02-diagnostico"))

    def test_write_artifact_creates_file_with_content(self) -> None:
        artifact = write_artifact(self.folder, "painel", "dados finais")
        self.assertTrue(artifact.exists())
        self.assertEqual(artifact.read_text(encoding="utf-8"), "dados finais")


if __name__ == "__main__":
    unittest.main()
