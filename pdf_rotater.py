#!/usr/bin/env python3

#
# pdf_rotater.py
#
# Date    : 2024-06-08
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
IN_DIR = '.\\input_rotater'
OUT_DIR = '.\\output_rotater'
ROTATE_ANGLE = 270    # 90, 180, 270


# Main
def main() -> None:

    in_file_list = list(Path(IN_DIR).glob("**/*.pdf"))
    for in_file_name in in_file_list:
        print('%s' % in_file_name)
        if os.path.isfile(in_file_name):
            in_file = open(in_file_name, 'rb')
            reader = PyPDF2.PdfReader(in_file)
            writer = PyPDF2.PdfWriter()
            for page in range(0, len(reader.pages)):
                obj = reader.pages[page]
                obj.rotate(ROTATE_ANGLE)
                writer.add_page(obj)
            _, out_file_name = os.path.split(in_file_name)
            in_file.close()
            out_file = open(os.path.join(OUT_DIR, out_file_name), 'wb')
            writer.write(out_file)
            out_file.close()

    sys.exit(0)


# Goto Main
if __name__ == '__main__':
    main()
