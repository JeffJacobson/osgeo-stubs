import enum
from enum import EnumType
from itertools import groupby
from pathlib import Path
from pprint import pformat
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
    return [f"osgeo.{n}" for n in ["gdal", "gdalconst", "ogr", "osr", "gnm"]]
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
        f"    {name} = {pformat(member.value)}"
        for name, member in cls.__members__.items()
    )

    return f"class {cls.__name__}({bases}):\n{members}"


def create_type_def(group_name: str, const_infos: dict[str, str | int | float]) -> str:
    """Creates Python type definition string.

    Args:
        group_name: Name of the type
        const_infos: dictionary of values

    Returns:
        A string with a type definition
    """
    members = (pformat(v) for v in const_infos.values())
    members = ",".join(members)
    output = f"type {group_name} = Literal[{members}]"
    return output


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
    enum_value_types: set[type] = set()
    for m in modules:
        # Create a list of constants for the current module
        current_constants = [*enumerate_constants(m)]

        for cc in current_constants:
            enum_value_types.add(type(cc.member_value))
        # Skip to next one if the list is empty
        if not (current_constants):
            continue
        # Create the output file path
        out_path = out_dir / f"{m.__name__.split(".")[-1]}_consts.py"
        # Open the file for writing text.
        with out_path.open("wt+") as f:
            print("import enum", "from typing import Literal", sep="\n", file=f)
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

                info = dict(info)
                enum_type = enum.Enum
                if all((isinstance(i, int) for i in info.values())):
                    enum_type = enum.IntEnum
                elif all((isinstance(i, str) for i in info.values())):
                    enum_type = enum.StrEnum
                print(create_type_def(group_name, info), file=f)

                try:
                    new_enum = enum_type(f"{group_name}Enum", info)
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
