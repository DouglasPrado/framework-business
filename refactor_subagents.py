#!/usr/bin/env python3
"""
Script para refatorar subagentes removendo código duplicado.

Remove métodos que agora estão na SubagentBase:
- _setup_directories() → setup_directories()
- _save_document() → save_document()
- _invoke_llm() → invoke_llm()
- _format_list() → format_list()
- _read_document() → read_document()

E atualiza chamadas para usar os métodos da base.
