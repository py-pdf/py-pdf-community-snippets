"""
Create a booklet-style PDF from a single input.

Pairs of two pages will be put on one page (left and right)

usage: python 2-up.py input_file output_file
"""

import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter


def main(pdf: Path, output: Path) -> None:
    reader = PdfReader(str(pdf))
    writer = PdfWriter()
    for i in range(0, len(reader.pages) - 1, 2):
        lhs = reader.pages[i]
        rhs = reader.pages[i + 1]
        lhs.merge_translated_page(
            rhs, tx=float(lhs.mediabox.width), ty=0, expand=True
        )
        writer.add_page(lhs)
        print(str(i) + " ")
        sys.stdout.flush()

    print(f"writing {output}")
    with open(output, "wb") as fp:
        writer.write(fp)
    print("done.")

def up2_main(pdf: Path, output: Path, layout: str = None) -> None:
    reader = PdfReader(str(pdf))
    writer = PdfWriter()

    if layout:
        # Define layout configurations (columns, rows) for each grid type
        layout_options = {
            "2x2": (2, 2),
            "3x3": (3, 3),
            "1x2": (1, 2),
            "2x1": (2, 1)
        }

        if layout not in layout_options:
            raise ValueError(f"Unsupported layout: {layout}")

        columns, rows = layout_options[layout]
        # Adjusted to use 'mediabox' instead of 'media_box'
        page_width = reader.pages[0].mediabox.width / columns
        page_height = reader.pages[0].mediabox.height / rows

        # Arrange pages in specified grid
        for i in range(0, len(reader.pages), columns * rows):
            new_page = writer.add_blank_page(width=reader.pages[0].mediabox.width,
                                             height=reader.pages[0].mediabox.height)
            
            for col in range(columns):
                for row in range(rows):
                    index = i + row * columns + col
                    if index < len(reader.pages):
                        page = reader.pages[index]
                        x_position = col * page_width
                        y_position = reader.pages[0].mediabox.height - (row + 1) * page_height
                        new_page.merge_translated_page(page, x_position, y_position)
    else:
        # Default behavior: add pages without grid layout
        for page in reader.pages:
            writer.add_page(page)
    
    with open(output, "wb") as f_out:
        writer.write(f_out)