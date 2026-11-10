import enum
from collections import OrderedDict
from enum import EnumType
from itertools import groupby
from pathlib import Path
from types import ModuleType
from typing import Annotated

import rich
import typer

from . import get_module
from .constants import enumerate_constants

_APP = typer.Typer()

def module_default_factory():
    """Sets the default modules if user omits them

    Returns:
        A list of strings, which are the names of modules
    """
    return [
        f"osgeo.{n}" for n in ["gdal", "gdalconst", "ogr", "osr", "gnm"]
    ]
    # return ["osgeo.gdal", "osgeo.gdalconst", "osgeo.ogr", "osgeo.osr"]


def enum_to_source(cls: EnumType) -> str:
    """Converts an Enum-derived class into Python code

    Args:
        cls: An enum class

    Returns:
        Python code to create that class.
    """
    bases = ", ".join(
        f"{base.__module__}.{base.__qualname__}" for base in cls.__bases__
    )

    members = "\n".join(
        f"    {name} = {member.value}" for name, member in cls.__members__.items()
    )

    return f"class {cls.__name__}({bases}):\n{members}"


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
    out_dir: Annotated[
        Path,
        typer.Argument(
            dir_okay=True,
            file_okay=False,
            help="Generated Python files defining enums will be written to this directory.",
        ),
    ] = Path(".", "src", "osgeo_enums"),
):
    """Creates Python enum definitions for the osgeo constants.

    Args:
        modules: a list of modules.
    """

    # Create the output directory if it does not already exist.
    out_dir.mkdir(exist_ok=True)
    for m in modules:
        current_constants = [*enumerate_constants(m)]
        if not(current_constants):
            continue
        # Create the output file path
        out_path = out_dir / f"{m.__name__.split(".")[-1]}_consts.py"
        with out_path.open("wt+") as f:
            print("import enum\n\n", file=f)
            g = groupby(current_constants, key=lambda x: x.prefix)
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
                    new_enum = enum.Enum(f"{group_name}Enum", info)
                    the_enums[group_name] = new_enum
                except TypeError:
                    rich.get_console().print_exception()
                else:
                    print(enum_to_source(new_enum), "\n\n", file=f)

    # print("import enum\n\n")

    # for k, v in the_enums.items():
    #     print(f"class {k}(enum.Enum):")
    #     for e in v:
    #         print("   ", e.name, "=", e.value)
    #     print("\n")
