#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Convert Kanseki Repository Mandoku-format (org-mode) files to json-lines."""

import jsonlines
import os
from pathlib import Path

from lib.util import clean_file, get_title

__author__ = "Nick Budak"
__email__ = "nbudak@princeton.edu"

# Where this script will load input and output processed texts
IN_DIR = Path("./org")
OUT_DIR = Path("./jsonl")


if __name__ == "__main__":
    """Clean each file in IN_DIR and output json-lines to OUT_DIR."""
    if not OUT_DIR.is_dir():
        os.mkdir(OUT_DIR)

    # convert all documents in org/ folder into json lines
    for path in IN_DIR.iterdir():
        if path.is_dir():
            print(f"{path.stem}")

            # create a new jsonl file to hold contents
            title = get_title(path)
            with jsonlines.open(f"{OUT_DIR}/{path.stem}.jsonl", mode="w") as writer:
                for file in sorted(list(path.glob("*.txt"))):

                    # ignore '000' files since they're usually ToCs / introductions
                    if "000.txt" in str(file):
                        continue

                    # clean and write as a line in .jsonl file
                    cleaned_file = clean_file(file)
                    writer.write(
                        {"id": file.stem, "series": path.stem, "text": cleaned_file}
                    )
