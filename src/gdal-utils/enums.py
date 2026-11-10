from collections import OrderedDict
import enum
from itertools import groupby
from types import ModuleType
from typing import Annotated

import rich
import typer

from . import get_module
from .constants import enumerate_constants
from .dump import module_default_factory

_APP = typer.Typer()


@_APP.command("enums")
def make_enums(
    modules: Annotated[
        list[ModuleType],
        typer.Argument(
            parser=get_module,
            default_factory=module_default_factory,
            help=f"Defaults: {module_default_factory()}",
        ),
    ],
    # out_file: Annotated[Path, typer.Option()] = Path("gdal_enums.py")
):
    """Creates Python enum definitions for the osgeo constants.

    Args:
        modules: Defaults to get_module, default_factory=module_default_factory, help=f"Defaults: {module_default_factory()}", ), ].
    """
    g = groupby(enumerate_constants(*modules), key=lambda x: x.prefix)
    the_enums: dict[str, enum.Enum] = {}
    for group_name, const_infos in g:
        if not group_name:
            continue

        info = [
            (ci.member_name, ci.member_value)
            for ci in const_infos
            if ci.prefix is not None
        ]

        info.sort(key=lambda t: t[1])

        info = OrderedDict(info)

        try:
            the_enums[group_name] = enum.Enum(group_name, info)
        except TypeError:
            rich.get_console().print_exception()

    print("import enum\n\n")

    for k, v in the_enums.items():
        print(f"class {k}(enum.Enum):")
        for e in v:
            print("   ", e.name, "=", e.value)
        print("\n")
