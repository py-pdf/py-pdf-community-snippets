"""
Define how the CLI should behave.

Subcommands are added here.
"""

from pathlib import Path
from typing import List, Optional

import typer
from typing_extensions import Annotated

import pdfly.booklet
import pdfly.cat
import pdfly.compress
import pdfly.extract_annotated_pages
import pdfly.extract_images
import pdfly.metadata
import pdfly.pagemeta
import pdfly.rm
import pdfly.uncompress
import pdfly.up2
import pdfly.update_offsets
import pdfly.x2pdf


def version_callback(value: bool) -> None:
    import pypdf

    if value:
        typer.echo(f"pdfly {pdfly.__version__}")
        typer.echo(f"  using pypdf=={pypdf.__version__}")
        raise typer.Exit


entry_point = typer.Typer(
    add_completion=False,
    help=(
        "pdfly is a pure-python cli application for manipulating PDF files."
    ),
    rich_markup_mode="rich",  # Allows to pretty-print commands documentation
)


@entry_point.callback()  # type: ignore[misc]
def common(
    ctx: typer.Context,
    version: bool = typer.Option(None, "--version", callback=version_callback),
) -> None:
    pass


@entry_point.command(name="extract-images", help=pdfly.extract_images.__doc__)  # type: ignore[misc]
def extract_images(
    pdf: Annotated[
        Path,
        typer.Argument(
            dir_okay=False,
            exists=True,
            resolve_path=True,
        ),
    ],
) -> None:
    pdfly.extract_images.main(pdf)


@entry_point.command(name="2-up", help=pdfly.up2.__doc__)  # type: ignore[misc]
def up2(
    pdf: Annotated[
        Path,
        typer.Argument(
            dir_okay=False,
            exists=True,
            resolve_path=True,
        ),
    ],
    out: Path,
) -> None:
    pdfly.up2.main(pdf, out)


@entry_point.command(name="cat", help=pdfly.cat.__doc__)  # type: ignore[misc]
def cat(
    filename: Annotated[
        Path,
        typer.Argument(
            dir_okay=False,
            exists=True,
            resolve_path=True,
        ),
    ],
    output: Path = typer.Option(..., "-o", "--output"),  # noqa
    fn_pgrgs: List[str] = typer.Argument(  # noqa
        ..., help="filenames and/or page ranges"
    ),
    verbose: bool = typer.Option(
        False, help="show page ranges as they are being read"
    ),
    password: str = typer.Option(
        None, help="Document's user or owner password."
    ),
) -> None:
    pdfly.cat.main(filename, fn_pgrgs, output, verbose, password=password)


@entry_point.command(name="booklet", help=pdfly.booklet.__doc__)  # type: ignore[misc]
def booklet(
    filename: Annotated[
        Path,
        typer.Argument(
            dir_okay=False,
            exists=True,
            resolve_path=True,
        ),
    ],
    output: Annotated[
        Path,
        typer.Argument(
            dir_okay=False,
            exists=False,
            resolve_path=False,
        ),
    ],
    blank_page: Annotated[
        Optional[Path],
        typer.Option(
            "-b",
            "--blank-page-file",
            help="page added if input is odd number of pages",
            dir_okay=False,
            exists=True,
            resolve_path=True,
        ),
    ] = None,
    centerfold: Annotated[
        Optional[Path],
        typer.Option(
            "-c",
            "--centerfold-file",
            help="double-page added if input is missing >= 2 pages",
            dir_okay=False,
            exists=True,
            resolve_path=True,
        ),
    ] = None,
) -> None:
    pdfly.booklet.main(filename, output, blank_page, centerfold)


@entry_point.command(name="rm", help=pdfly.rm.__doc__)
def rm(
    filename: Annotated[
        Path,
        typer.Argument(
            dir_okay=False,
            exists=True,
            resolve_path=True,
        ),
    ],
    output: Path = typer.Option(..., "-o", "--output"),  # noqa
    fn_pgrgs: List[str] = typer.Argument(  # noqa
        ..., help="filenames and/or page ranges"
    ),
    verbose: bool = typer.Option(
        False, help="show page ranges as they are being read"
    ),
) -> None:
    pdfly.rm.main(filename, fn_pgrgs, output, verbose)


@entry_point.command(name="meta", help=pdfly.metadata.__doc__)  # type: ignore[misc]
def metadata(
    pdf: Annotated[
        Path,
        typer.Argument(
            dir_okay=False,
            exists=True,
            resolve_path=True,
        ),
    ],
    output: pdfly.metadata.OutputOptions = typer.Option(  # noqa
        pdfly.metadata.OutputOptions.text.value,
        "--output",
        "-o",
        help="output format",
        show_default=True,
    ),
) -> None:
    pdfly.metadata.main(pdf, output)


@entry_point.command(name="pagemeta", help=pdfly.pagemeta.__doc__)  # type: ignore[misc]
def pagemeta(
    pdf: Annotated[
        Path,
        typer.Argument(
            dir_okay=False,
            exists=True,
            resolve_path=True,
        ),
    ],
    page_index: int,
    output: pdfly.metadata.OutputOptions = typer.Option(  # noqa
        pdfly.metadata.OutputOptions.text.value,
        "--output",
        "-o",
        help="output format",
        show_default=True,
    ),
) -> None:
    pdfly.pagemeta.main(
        pdf,
        page_index,
        output,
    )


@entry_point.command(name="extract-text")  # type: ignore[misc]
def extract_text(
    pdf: Annotated[
        Path,
        typer.Argument(
            dir_okay=False,
            exists=True,
            resolve_path=True,
        ),
    ],
) -> None:
    """Extract text from a PDF file."""
    from pypdf import PdfReader

    reader = PdfReader(str(pdf))
    for page in reader.pages:
        typer.echo(page.extract_text())


@entry_point.command(name="compress", help=pdfly.compress.__doc__)  # type: ignore[misc]
def compress(
    pdf: Annotated[
        Path,
        typer.Argument(
            dir_okay=False,
            exists=True,
            resolve_path=True,
        ),
    ],
    output: Annotated[
        Path,
        typer.Argument(
            writable=True,
        ),
    ],
) -> None:
    pdfly.compress.main(pdf, output)


@entry_point.command(name="uncompress", help=pdfly.uncompress.__doc__)  # type: ignore[misc]
def uncompress(
    pdf: Annotated[
        Path,
        typer.Argument(
            dir_okay=False,
            exists=True,
            resolve_path=True,
        ),
    ],
    output: Annotated[
        Path,
        typer.Argument(
            writable=True,
        ),
    ],
) -> None:
    pdfly.uncompress.main(pdf, output)


@entry_point.command(name="update-offsets", help=pdfly.update_offsets.__doc__)  # type: ignore[misc]
def update_offsets(
    file_in: Annotated[
        Path,
        typer.Argument(
            dir_okay=False,
            exists=True,
            resolve_path=True,
        ),
    ],
    file_out: Path,
    encoding: str = typer.Option(
        "ISO-8859-1",
        help="Encoding used to read and write the files, e.g. UTF-8.",
    ),
    verbose: bool = typer.Option(
        False, help="Show progress while processing."
    ),
) -> None:
    pdfly.update_offsets.main(file_in, file_out, encoding, verbose)


@entry_point.command(name="x2pdf", help=pdfly.x2pdf.__doc__)  # type: ignore[misc]
def x2pdf(
    x: List[
        Annotated[
            Path,
            typer.Argument(
                dir_okay=False,
                exists=True,
                resolve_path=True,
            ),
        ]
    ],
    output: Annotated[
        Path,
        typer.Option(
            "-o",
            "--output",
            writable=True,
        ),
    ],
) -> None:
    exit_code = pdfly.x2pdf.main(x, output)
    if exit_code:
        raise typer.Exit(code=exit_code)


@entry_point.command(name="extract-annotated-pages", help=pdfly.extract_annotated_pages.__doc__)  # type: ignore[misc]
def extract_annotated_pages(
    input_pdf: Annotated[
        Path,
        typer.Argument(
            dir_okay=False,
            exists=True,
            resolve_path=True,
            help="Input PDF file.",
        ),
    ],
    output_pdf: Annotated[
        Optional[Path],
        typer.Option(
            "--output",
            "-o",
            writable=True,
            help="Output PDF file. Defaults to 'input_pdf_annotated'.",
        ),
    ] = None,
) -> None:
    pdfly.extract_annotated_pages.main(input_pdf, output_pdf)
