# -*- coding: utf-8 -*-
# -- This file is part of the Apio project
# -- (C) 2016-2024 FPGAwars
# -- Authors
# --  * Jesús Arroyo (2016-2019)
# --  * Juan Gonzalez (obijuan) (2019-2024)
# -- Licence GPLv2
"""Main implementation of APIO BOARDS command"""

from pathlib import Path
import click
from click.core import Context
from apio.resources import Resources
from apio import util
from apio.commands import options

# ---------------------------
# -- COMMAND SPECIFIC OPTIONS
# ---------------------------
list_fpgas_option = click.option(
    "fpgas",  # Var name
    "-f",
    "--fpga",
    is_flag=True,
    help="List supported FPGA chips.",
)


# ---------------------------
# -- COMMAND
# ---------------------------
HELP = """
The boards commands lists the FPGA boards and chips that are
supported by apio.
The commands is typically used in the root directory
of the project that contains the apio.ini file.

\b
Examples:
  apio boards --list  # List boards
  apio boards --fpga  # List FPGAs

[Advanced] Boards with wide availability can be added by contacting the
apio team. A custom one-of board can be added to your project by
placing a boards.json file next to apio.ini.
"""


@click.command(
    "boards",
    short_help="List supported boards and FPGAs.",
    help=HELP,
    context_settings=util.context_settings(),
)
@click.pass_context
@options.project_dir_option
@options.list_option_gen(help="List supported FPGA boards.")
@list_fpgas_option
def cli(
    ctx: Context,
    # Options
    project_dir: Path,
    list_: bool,
    fpgas: bool,
):
    """Implements the 'boards' command which lists supported boards
    and FPGAs.
    """

    # pylint: disable=fixme
    # TODO: Exit with error status if both --list and --fpga are specified.

    # pylint: disable=fixme
    # TODO: rename options --list, --fpga to --boards, --fpgas.

    # -- Access to the apio resources
    resources = Resources(project_dir=project_dir)

    # -- Option 1: List boards
    if list_:
        resources.list_boards()

    # -- Option 2: List fpgas
    elif fpgas:
        resources.list_fpgas()

    # -- No options: show help
    else:
        click.secho(ctx.get_help())
