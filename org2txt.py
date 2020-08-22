#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Convert Kanseki Repository Mandoku-format (org-mode) files to plaintext."""

import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, Match

__author__ = "Nick Budak"
__email__ = "nbudak@princeton.edu"

# Regular expressions used to find and transform non-text content
COMMENTARY_RE = re.compile(r"\([^\)]+\)(¶\n)?")
PB_RE = re.compile(r"<pb:([^>]+)>")
EMPTY_LINE_RE = re.compile(r"^\s+\n$")
WS_RE = re.compile(r"\n{3,}")
KR_ENTITY_RE = re.compile(r"&(KR\d+);")

# Titles of books that contain text sources; should be stripped from output
TEXT_BOOKS = ["欽定四庫全書"]

# Metadata table - titles, etc.
with open("metadata.json") as file:
    METADATA: Dict = json.loads(file.read())

# Unicode private use characters that replace html entities and other gaiji
with open("gaiji.json") as file:
    GAIJI: Dict = json.loads(file.read())


def get_unicode(match: Match[str]) -> str:
    """Return the unicode private use representation for a special entity."""
    return GAIJI.get(match.group(1), None)


def get_title(path: Any) -> str:
    """Get the title of the text files in a document directory as a string."""
    if not path.is_dir():
        raise NotADirectoryError(path)

    # fetch title from metadata table by Kanripo ID (path stem)
    return METADATA.get(path.stem, None)


def clean_doc(path: Any) -> str:
    """Convert a directory of org-mode text files into a cleaned string."""
    if not path.is_dir():
        raise NotADirectoryError(path)

    # clean all text files and add to output
    cleaned_output = ""
    for file in sorted(list(path.glob("*.txt"))):
        # ignore '000' files since they're usually ToCs, introductions, etc.
        if "000.txt" in str(file):
            continue
        cleaned_output += clean_file(file)
    return cleaned_output


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
        if line.strip() in TEXT_BOOKS:
            continue
        # strip out commentary (parentheticals)
        cleaned_line = COMMENTARY_RE.sub("", line)
        # strip out page breaks
        cleaned_line = PB_RE.sub("", cleaned_line)
        # strip out paragraph markers (¶)
        cleaned_line = cleaned_line.replace("¶", "")
        # replace kanripo entities with private use unicode
        cleaned_line = KR_ENTITY_RE.sub(get_unicode, cleaned_line)
        # ignore lines with only whitespace
        if not EMPTY_LINE_RE.match(cleaned_line):
            cleaned_output += cleaned_line

    # collapse consecutive whitespace
    cleaned_output = WS_RE.sub("\n\n", cleaned_output)
    return cleaned_output


if __name__ == "__main__":
    # create the txt/ folder if it doesn't exist
    if not Path("txt/").is_dir():
        os.mkdir("txt")

    # convert all documents in org/ folder into plaintext
    for doc in Path("org/").iterdir():
        if doc.is_dir():
            # get title and cleaned text
            title = get_title(doc)
            cleaned_doc = clean_doc(doc)
            # write to a new file in txt/ folder
            new_file = Path(f"txt/{title}.txt")
            with new_file.open("w") as file:
                file.write(cleaned_doc)
