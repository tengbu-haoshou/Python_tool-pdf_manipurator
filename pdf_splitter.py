#!/usr/bin/env python3

#
# pdf_rotater.py
#
# Date    : 2024-06-09
# Auther  : Hirotoshi FUJIBE
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
IN_DIR = '.\\input_splitter'
OUT_DIR = '.\\output_splitter'
NUM_FORMAT = '_%.2s'


# Main
def main() -> None:

    in_file_list = list(Path(IN_DIR).glob("**/*.pdf"))
    for in_file_name in in_file_list:
        print('%s' % in_file_name)
        if os.path.isfile(in_file_name):
            in_file = open(in_file_name, 'rb')
            reader = PyPDF2.PdfReader(in_file)
            _, file_name = os.path.split(in_file_name)
            file_name, ext = os.path.splitext(file_name)
            for page in range(0, len(reader.pages)):
                writer = PyPDF2.PdfWriter()
                obj = reader.pages[page]
                writer.add_page(obj)
                out_file_name = os.path.join(OUT_DIR, file_name + NUM_FORMAT % (page + 1) + ext)
                out_file = open(out_file_name, 'wb')
                writer.write(out_file)
                out_file.close()
            in_file.close()

    sys.exit(0)


# Goto Main
if __name__ == '__main__':
    main()
