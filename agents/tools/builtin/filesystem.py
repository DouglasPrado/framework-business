"""Ferramentas de sistema de arquivos implementadas como LangChain tools."""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Iterable, List

from langchain_core.tools import StructuredTool

from ... import BASE_PATH


def _ls(path: str = ".", recursive: bool = False) -> str:
    target = (BASE_PATH / path).resolve()
    if not target.exists():
        raise ValueError(f"Caminho {path} não encontrado.")
    if recursive:
        lines: List[str] = []
        for root, dirs, files in os.walk(target):
            rel_root = Path(root).relative_to(BASE_PATH)
            lines.append(str(rel_root) + ":")
            for entry in sorted(dirs + files):
                lines.append(f"  - {entry}")
        return "\n".join(lines)
    entries = sorted(p.name for p in target.iterdir())
    return "\n".join(entries)


def _read_file(path: str) -> str:
    target = (BASE_PATH / path).resolve()
    if not target.exists() or not target.is_file():
        raise ValueError(f"Arquivo {path} não encontrado.")
    return target.read_text(encoding="utf-8")


def _write_file(path: str, content: str) -> str:
    target = (BASE_PATH / path).resolve()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    return str(target)


def _edit_file(path: str, pattern: str, replacement: str, count: int = 0) -> str:
    target = (BASE_PATH / path).resolve()
    if not target.exists():
        raise ValueError(f"Arquivo {path} não encontrado.")
    text = target.read_text(encoding="utf-8")
    new_text, replaced = re.subn(pattern, replacement, text, count=count)
    target.write_text(new_text, encoding="utf-8")
    return f"{replaced} ocorrências substituídas."


def _glob(pattern: str) -> str:
    matches = sorted(str(p.relative_to(BASE_PATH)) for p in BASE_PATH.glob(pattern))
    return "\n".join(matches)


def _grep(pattern: str, path: str = ".") -> str:
    target = (BASE_PATH / path).resolve()
    files: Iterable[Path]
    if target.is_dir():
        files = target.rglob("*")
    else:
        files = [target]
    regex = re.compile(pattern)
    lines: List[str] = []
    for file_path in files:
        if not file_path.is_file():
            continue
        try:
            content = file_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for idx, line in enumerate(content.splitlines(), start=1):
            if regex.search(line):
                rel = file_path.relative_to(BASE_PATH)
                lines.append(f"{rel}:{idx}: {line}")
    return "\n".join(lines)


LS_TOOL = StructuredTool.from_function(
    _ls,
    name="ls",
    description="Lista arquivos e diretórios relativos ao repositório.",
)

READ_FILE_TOOL = StructuredTool.from_function(
    _read_file,
    name="read_file",
    description="Lê o conteúdo integral de um arquivo UTF-8.",
)

WRITE_FILE_TOOL = StructuredTool.from_function(
    _write_file,
    name="write_file",
    description="Escreve (sobrescreve) um arquivo com texto UTF-8.",
)

EDIT_FILE_TOOL = StructuredTool.from_function(
    _edit_file,
    name="edit_file",
    description="Aplica substituições regex em um arquivo de texto.",
)

GLOB_TOOL = StructuredTool.from_function(
    _glob,
    name="glob",
    description="Lista arquivos que correspondem a um padrão glob.",
)

GREP_TOOL = StructuredTool.from_function(
    _grep,
    name="grep",
    description="Busca expressões regulares em arquivos.",
)


FILE_SYSTEM_TOOLS = [
    LS_TOOL,
    READ_FILE_TOOL,
    WRITE_FILE_TOOL,
    EDIT_FILE_TOOL,
    GLOB_TOOL,
]

SEARCH_TOOLS = [GREP_TOOL]
