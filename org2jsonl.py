#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Convert Kanseki Repository Mandoku-format (org-mode) files to jsonl."""

import json
import jsonlines
import os
import re
from pathlib import Path
from typing import Any, Dict, Match

__author__ = "Nick Budak"
__email__ = "nbudak@princeton.edu"

# Regular expressions used to find and transform non-text content
COMMENTARY_RE = re.compile(r"(¶\n)?\([^\)]+\)(¶\n)?")
PB_RE = re.compile(r"(¶\n)?<pb:([^>]+)>(¶\n)?")
EMPTY_LINE_RE = re.compile(r"^\s+\n$")
WS_RE = re.compile(r"\n{3,}")
KR_ENTITY_RE = re.compile(r"&(KR\d+);")
CHAR_COMBO_RE = re.compile(r"\[[^\]]+\]")

# Titles of books that contain text sources; should be stripped from output
TEXT_BOOKS = ["欽定四庫全書"]

# Where this script will load input and output processed texts
IN_DIR = Path("./org")
OUT_DIR = Path("./jsonl")

# Metadata table - titles, etc.
with open("metadata.json") as file:
    METADATA: Dict = json.loads(file.read())

# Unicode private use characters that replace html entities and other gaiji
with open("gaiji.json") as file:
    GAIJI: Dict = json.loads(file.read())


def get_entity_unicode(match: Match[str]) -> str:
    """Return the unicode private use representation for a special entity."""
    return GAIJI.get(match.group(1), None)


def get_combo_unicode(match: Match[str]) -> str:
    """Return the unicode private use representation for character combos."""
    return GAIJI.get(match.group(0), None)


def get_title(path: Any) -> str:
    """Get the title of the text files in a document directory as a string."""
    if not path.is_dir():
        raise NotADirectoryError(path)

    # fetch title from metadata table by Kanripo ID (path stem)
    return METADATA.get(path.stem, None)


def clean_file(path: Any) -> str:
    """Convert a single org-mode text file into a cleaned string."""
    if not path.is_file():
        raise FileNotFoundError(path)

    # clean each line in the file and add to output
    cleaned_output = ""
    with path.open() as file:
        lines = file.readlines()
    for line in lines:
        # ignore comments and metadata
        if line.startswith("#"):
            continue
        # ignore names of books from which texts are drawn
        if any(book in line for book in TEXT_BOOKS):
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


if __name__ == "__main__":
    # create the jsonl/ folder if it doesn't exist
    if not OUT_DIR.is_dir():
        os.mkdir(OUT_DIR)

    # convert all documents in org/ folder into json lines
    for path in IN_DIR.iterdir():
        if path.is_dir():

            # create a new jsonl file to hold contents
            title = get_title(path)
            with jsonlines.open(f"{OUT_DIR}/{path.stem}.jsonl", mode="w") as writer:
                for file in sorted(list(path.glob("*.txt"))):

                    # ignore '000' files since they're usually ToCs / introductions
                    if "000.txt" in str(file):
                        continue

                    # clean and write as a line in .jsonl file
                    cleaned_file = clean_file(file)
                    writer.write({
                        "id": file.stem,
                        "series": path.stem,
                        "text": cleaned_file
                    })
