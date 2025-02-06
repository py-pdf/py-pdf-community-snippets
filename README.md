[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PyPI version](https://badge.fury.io/py/pdfly.svg)](https://pypi.org/project/pdfly/)
[![GitHub last commit](https://img.shields.io/github/last-commit/py-pdf/pdfly)](https://github.com/py-pdf/pdfly)
[![Python Support](https://img.shields.io/pypi/pyversions/pdfly.svg)](https://pypi.org/project/pdfly/)
[![Documentation Status](https://readthedocs.org/projects/pdfly/badge/?version=latest)](https://pdfly.readthedocs.io/en/latest/?badge=latest)
[![](https://img.shields.io/badge/-documentation-green)](https://pdfly.readthedocs.io/en/latest/)

# pdfly

pdfly (say: PDF-li) is a pure-python cli application for manipulating PDF files.

## Installation

```bash
pip install -U pdfly
```

As `pdfly` is an application, you might want to install it with [`pipx`](https://pypi.org/project/pipx/).

## Usage

```console
$ pdfly --help

 Usage: pdfly [OPTIONS] COMMAND [ARGS]...

 pdfly is a pure-python cli application for manipulating PDF files.

╭─ Options ────────────────────────────────────────────────────────────────────────────╮
│ --version                                                                            │
│ --help                    Show this message and exit.                                │
╰──────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────────────╮
│ 2-up                      Create a booklet-style PDF from a single input.            │
│ cat                       Concatenate pages from PDF files into a single PDF file.   │
│ compress                  Compress a PDF.                                            │
| uncompress                Uncompresses a PDF.                                        │
| extract-annotated-pages   Extract only the annotated pages from a PDF.               |
│ extract-images            Extract images from PDF without resampling or altering.    │
│ extract-text              Extract text from a PDF file.                              │
│ meta                      Show metadata of a PDF file                                │
│ pagemeta                  Give details about a single page.                          │
│ rm                        Remove pages from PDF files.                               │
│ update-offsets            Updates offsets and lengths in a simple PDF file.          │
│ x2pdf                     Convert one or more files to PDF. Each file is a page.     │
╰──────────────────────────────────────────────────────────────────────────────────────╯
```

You can see the help of every subcommand by typing:

```console
$ pdfly 2-up --help

 Usage: pdfly 2-up [OPTIONS] PDF OUT

 Create a booklet-style PDF from a single input.
 Pairs of two pages will be put on one page (left and right)
 usage: python 2-up.py input_file output_file

╭─ Arguments ──────────────────────────────────────────────────────────────────────────╮
│ *    pdf      PATH  [default: None] [required]                                       │
│ *    out      PATH  [default: None] [required]                                       │
╰──────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                          │
╰──────────────────────────────────────────────────────────────────────────────────────╯
```

## Contributors ✨

pdfly is a free software project without any company affiliation. We cannot pay
contributors, but we do value their contributions 🤗

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="20%"><a href="http://martin-thoma.com/"><img src="https://avatars.githubusercontent.com/u/1658117?v=4?s=100" width="100px;" alt="Martin Thoma"/><br /><sub><b>Martin Thoma</b></sub></a><br /><a href="https://github.com/py-pdf/pdfly/commits?author=MartinThoma" title="Code">💻</a> <a href="https://github.com/py-pdf/pdfly/commits?author=MartinThoma" title="Documentation">📖</a> <a href="#ideas-MartinThoma" title="Ideas, Planning, & Feedback">🤔</a> <a href="#infra-MartinThoma" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="#maintenance-MartinThoma" title="Maintenance">🚧</a> <a href="#projectManagement-MartinThoma" title="Project Management">📆</a> <a href="#tutorial-MartinThoma" title="Tutorials">✅</a></td>
      <td align="center" valign="top" width="20%"><a href="https://chezsoi.org/lucas/blog/"><img src="https://avatars.githubusercontent.com/u/925560?v=4?s=100" width="100px;" alt="Lucas Cimon"/><br /><sub><b>Lucas Cimon</b></sub></a><br /><a href="https://github.com/py-pdf/pdfly/issues?q=author%3ALucas-C" title="Bug reports">🐛</a> <a href="https://github.com/py-pdf/pdfly/commits?author=Lucas-C" title="Code">💻</a> <a href="https://github.com/py-pdf/pdfly/commits?author=Lucas-C" title="Documentation">📖</a> <a href="#maintenance-Lucas-C" title="Maintenance">🚧</a></td>
      <td align="center" valign="top" width="20%"><a href="https://github.com/pastor-robert"><img src="https://avatars.githubusercontent.com/u/35646090?v=4?s=100" width="100px;" alt="Rob Adams"/><br /><sub><b>Rob Adams</b></sub></a><br /><a href="https://github.com/py-pdf/pdfly/commits?author=pastor-robert" title="Code">💻</a></td>
      <td align="center" valign="top" width="20%"><a href="https://github.com/Kaos599"><img src="https://avatars.githubusercontent.com/u/115716485?v=4?s=100" width="100px;" alt="Harsh "/><br /><sub><b>Harsh </b></sub></a><br /><a href="https://github.com/py-pdf/pdfly/commits?author=Kaos599" title="Code">💻</a></td>
      <td align="center" valign="top" width="20%"><a href="https://github.com/srogmann"><img src="https://avatars.githubusercontent.com/u/59577610?v=4?s=100" width="100px;" alt="Sascha Rogmann"/><br /><sub><b>Sascha Rogmann</b></sub></a><br /><a href="https://github.com/py-pdf/pdfly/commits?author=srogmann" title="Code">💻</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="20%"><a href="https://github.com/ebotiab"><img src="https://avatars.githubusercontent.com/u/62219950?v=4?s=100" width="100px;" alt="Enrique Botía"/><br /><sub><b>Enrique Botía</b></sub></a><br /><a href="https://github.com/py-pdf/pdfly/commits?author=ebotiab" title="Code">💻</a></td>
      <td align="center" valign="top" width="20%"><a href="https://github.com/kommade"><img src="https://avatars.githubusercontent.com/u/99523586?v=4?s=100" width="100px;" alt="kommade"/><br /><sub><b>kommade</b></sub></a><br /><a href="https://github.com/py-pdf/pdfly/commits?author=kommade" title="Code">💻</a></td>
      <td align="center" valign="top" width="20%"><a href="https://spoo.me/"><img src="https://avatars.githubusercontent.com/u/90309290?v=4?s=100" width="100px;" alt="Zingzy"/><br /><sub><b>Zingzy</b></sub></a><br /><a href="https://github.com/py-pdf/pdfly/commits?author=Zingzy" title="Code">💻</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification
([emoji key](https://allcontributors.org/docs/en/emoji-key)).
Contributions of any kind welcome!

The list might not be complete. You can find more contributors via the git
history and [GitHubs 'Contributors' feature](https://github.com/py-pdf/pdfly/graphs/contributors).
