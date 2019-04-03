#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# strip trailing whitespace and hard carriage returns
# requires python >= 3.6

from pathlib import Path
from typing import List, Dict
from text_colors import color_encode, color_print

usage_blob=\
    '''
strip_cr.py
    
SYNOPSIS
    strip_cr [FILE_LIST]

DESCRIPTION
    Strip trailing whitespace and hard carriage returns from files
        in FILE_LIST; Requires Python >= 3.6

    parameter:
        files (list[str])       : 1 or more files to strip
    return:
        result (list[str])      : list of failures (empty = success)
    '''

HEADER = color_encode("COLOR15", "BG_BLACK", "ITALIC")
MAIN = color_encode("MAIN", "BG_BLACK", "ITALIC")
BLUE = color_encode("COOL", "BG_BLACK", "ITALIC")
PURPLE = color_encode("PURPLE", "BG_BLACK", "ITALIC")
RESET = color_encode("PURPLE", "RESET", "ITALIC")


def strip_cr(files: List[str]) -> List[str]:
    """
        strip_cr: strip trailing whitespace and hard carriage returns

        parameter:
            files (list)        : 1 or more files to sort
        return:
            result (list)       : list of failures (empty = success)
        """
    from pathlib import Path

    result: List[str] = []
    file: str = ""

    for file in files:
        try:
            p: object = Path(file)
        except OSError as e:
            result.append(file)
        else:
            raw_text: str = p.read_text()
            out_text: str = '\n'.join([line.rstrip(" \r") for line in raw_text])
            p.write_text(out_text)
    return result


if __name__ == "__main__":
    import sys
    # ? Used if run as CLI utility
    arg = ""
    if len(sys.argv) < 2:
        print(usage_blob)
    else:
        args = sys.argv[1:]

        # ? TEST DATA
        print(PURPLE)
        print("Output for strip_cr module:")
        print("MIT license  |  copyright (c) 2018 Michael Treanor")
        print("<https://www.github.com/skeptycal")
        print(BLUE)
        print("List of files: ")
        print(HEADER, args)
        print()
        result = strip_cr(args)
