#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Convert Kanseki Repository Mandoku-format (org-mode) files to plaintext."""

import json
import os
import re
import sys
from pathlib import Path
from typing import Any

__author__ = "Nick Budak"
__email__ = "nbudak@princeton.edu"

# Regular expressions used to find non-text content
TITLE_RE = re.compile(r"^#\+TITLE: (.+)$")
COMMENTARY_RE = re.compile(r"\([^\)]+\)")
PB_RE = re.compile(r"<pb:([^>]+)>")

# Titles of books that contain text sources; should be stripped from output
TEXT_BOOKS = ["欽定四庫全書"]

# Metadata table - titles, etc.
with open("metadata.json") as file:
    METADATA = json.loads(file.read())

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
        # strip out paragraph markers (¶)
        cleaned_line = line.replace("¶", "")
        # ignore names of books from which texts are drawn
        if cleaned_line.strip() in TEXT_BOOKS:
            continue
        # strip out commentary (parentheticals)
        cleaned_line = COMMENTARY_RE.sub("", cleaned_line)
        # strip out page breaks
        cleaned_line = PB_RE.sub("", cleaned_line)
        cleaned_output += cleaned_line
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
