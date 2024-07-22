#!/usr/bin/env python3

#
# pdf_merger.py
#
# Date    : 2024-06-05
# Author  : Hirotoshi FUJIBE
# History :
#
# Copyright (c) 2024 Hirotoshi FUJIBE
#

# Import Libraries
import os
import sys
import PyPDF2
from pathlib import Path

# Constants
IN_DIR = '.\\input_merger'
OUT_DIR = '.\\output_merger'
OUT_NAME = 'merged.pdf'


# Main
def main() -> None:

    merger = PyPDF2.PdfMerger()

    in_file_list = list(Path(IN_DIR).glob("**/*.pdf"))
    for in_file_name in in_file_list:
        print('%s' % in_file_name)
        if os.path.isfile(in_file_name):
            merger.append(in_file_name)

    merger.write(os.path.join(OUT_DIR, OUT_NAME))
    merger.close()

    sys.exit(0)


# Goto Main
if __name__ == '__main__':
    main()
