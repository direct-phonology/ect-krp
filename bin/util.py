#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Utilities for Kanseki Repository Mandoku-format (org-mode) files."""

import re
import json
from typing import Match
from pathlib import Path

# Regular expressions used to find and transform text content
METADATA_RE = re.compile(r"^\s*[漢晉].*[撰注舒]¶$")
TITLE_RE = re.compile(r"^\*{2,3}")
SECTION_RE = re.compile(r"^\s*\S{0,8}[第卷][一二三四五六七八九]?十?[一二三四五六七八九上十下中][¶\s]")
COMMENTARY_RE = re.compile(r"(¶\n)?\([^\)]+\)(¶\n)?")
PB_RE = re.compile(r"(¶\n)?<pb:([^>]+)>(¶\n)?")
EMPTY_LINE_RE = re.compile(r"^\s+\n$")
WS_RE = re.compile(r"\n{3,}")
KR_ENTITY_RE = re.compile(r"&(KR\d+);")
CHAR_COMBO_RE = re.compile(r"\[[^\]]+\]")

# Titles of books that contain text sources; should be stripped from output
TEXT_BOOKS = ["欽定四庫全書"]

# Unicode private use characters that replace html entities and other gaiji
with open("gaiji.json") as file:
    GAIJI: dict = json.loads(file.read())

# Metadata table - titles, etc.
with open("metadata.json") as file:
    METADATA: dict = json.loads(file.read())


def get_entity_unicode(match: Match[str]) -> str:
    """Return the unicode private use representation for a special entity."""
    try:
        return GAIJI[match.group(1)]
    except KeyError:
        raise UserWarning(f"Special entity not found: {match.group(1)}")


def get_combo_unicode(match: Match[str]) -> str:
    """Return the unicode private use representation for character combos."""
    # If no entry in GAIJI, return the original character
    return GAIJI.get(match.group(0), match.group(0))


def get_title(path: Path) -> str:
    """Convert a directory path like KR1a0001 into the text's Chinese name."""
    if not path.is_dir():
        raise NotADirectoryError(path)

    # fetch title from metadata table by Kanripo ID (path stem)
    return METADATA.get(path.stem, None)


def clean_file(path: Path) -> str:
    """Convert a single org-mode text file into a cleaned string."""
    if not path.is_file():
        raise FileNotFoundError(path)

    # clean each line in the file and add to output
    cleaned_output = ""
    with path.open() as file:
        lines = file.readlines()
    for line in lines:
        # ignore comments
        if line.startswith("#"):
            continue
        # ignore any line with a TEXT_BOOK name in it
        if any(book in line for book in TEXT_BOOKS):
            continue
        # ignore lines that are metadata (dynasty, author, etc.)
        if METADATA_RE.match(line):
            continue
        # ignore lines that are section/title headers
        if SECTION_RE.match(line) or TITLE_RE.match(line):
            continue
        # strip out page breaks
        cleaned_line = PB_RE.sub("", line)
        # strip out paragraph markers (¶)
        cleaned_line = cleaned_line.replace("¶", "")
        # replace kanripo entities with private use unicode
        cleaned_line = KR_ENTITY_RE.sub(get_entity_unicode, cleaned_line)
        # replace combo characters like [a+b] with private use unicode
        cleaned_line = CHAR_COMBO_RE.sub(get_combo_unicode, cleaned_line)
        # strip out commentary (parentheticals)
        cleaned_line = COMMENTARY_RE.sub("", cleaned_line)
        # ignore lines with only whitespace
        if not EMPTY_LINE_RE.match(cleaned_line):
            cleaned_output += cleaned_line

    # collapse consecutive whitespace
    cleaned_output = WS_RE.sub("\n\n", cleaned_output)
    return cleaned_output
