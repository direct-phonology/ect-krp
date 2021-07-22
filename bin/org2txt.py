#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Convert Kanseki Repository Mandoku-format (org-mode) files to plaintext."""

import os
from pathlib import Path

from util import clean_file

__author__ = "Nick Budak"
__email__ = "nbudak@princeton.edu"

# Where this script will load input and output processed texts
IN_DIR = Path("./org")
OUT_DIR = Path("./txt")


if __name__ == "__main__":
    """Clean each file in IN_DIR and output plaintext to OUT_DIR."""
    if not OUT_DIR.is_dir():
        os.mkdir(OUT_DIR)

    # convert all documents in IN_DIR folder into plaintext
    for path in IN_DIR.iterdir():
        if path.is_dir():
            print(f"{path.stem}")

            # create a directory for all files in this doc
            if not Path(f"{OUT_DIR}/{path.stem}").is_dir():
                os.mkdir(f"{OUT_DIR}/{path.stem}")

            # clean each file and store in new doc directory
            for file in sorted(list(path.glob("*.txt"))):

                # ignore '000' files since they're usually ToCs / introductions
                if "000.txt" in str(file):
                    continue
                cleaned_file = clean_file(file)

                # write to a new file in txt/ folder
                new_file = Path(f"{OUT_DIR}/{path.stem}/{file.name}")
                with new_file.open("w") as fh:
                    fh.write(cleaned_file)
                print(f"\t{file.name}")
