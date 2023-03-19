"""Give details about a single page."""

from pathlib import Path
from typing import Tuple
from pydantic import BaseModel
from pypdf import PdfReader

from ._utils import OutputOptions


class PageMeta(BaseModel):
    mediabox: Tuple[int, int, int, int]
    cropbox: Tuple[int, int, int, int]
    artbox: Tuple[int, int, int, int]
    bleedbox: Tuple[int, int, int, int]
    annotations: int


def main(pdf: Path, page_index: int, output: OutputOptions):
    reader = PdfReader(pdf)
    page = reader.pages[page_index]
    meta = PageMeta(
        mediabox=page.mediabox,
        cropbox=page.cropbox,
        artbox=page.artbox,
        bleedbox=page.bleedbox,
        annotations=len(page.annotations) if page.annotations else 0,
    )

    if output == OutputOptions.json:
        print(meta.json())
    else:
        from rich.console import Console
        from rich.table import Table
        from rich.markdown import Markdown

        console = Console()

        table = Table(title=f"{pdf}, page index {page_index}")
        table.add_column("Attribute", justify="right", style="cyan", no_wrap=True)
        table.add_column("Value", style="white")

        table.add_row("mediabox", str(meta.mediabox))
        table.add_row("cropbox", str(meta.cropbox))
        table.add_row("artbox", str(meta.artbox))
        table.add_row("bleedbox", str(meta.bleedbox))

        table.add_row("annotations", str(meta.annotations))

        console.print(table)

        if page.annotations:
            console.print(Markdown("**All annotations:**"))
            for i, annot in enumerate(page.annotations, start=1):
                obj = annot.get_object()
                console.print(f"{i}. {obj['/Subtype']} at {obj['/Rect']}")
