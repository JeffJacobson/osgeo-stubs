"""This script is a work in progress for, when it is finished,
will generate osgeo package type stubs.

Currently, the output needs to be further modified,
and files renamed and moved.

This would go beyond what alg_types.py does, also working with osgeo.
"""

from pathlib import Path
from types import ModuleType
from typing import Annotated

import typer

from . import MemberInfo, enumerate_modules, format_value, get_module

_APP = typer.Typer()


def module_default_factory():
    """Sets the default modules if user omits them

    Returns:
        A list of strings, which are the names of modules
    """
    return [
        f"osgeo.{n}" for n in ["gdal", "gdalconst", "ogr", "osr", "gdal_array", "gnm"]
    ]
    # return ["osgeo.gdal", "osgeo.gdalconst", "osgeo.ogr", "osgeo.osr"]


@_APP.command("stubs")
def make_stubs(
    modules: Annotated[
        list[ModuleType],
        typer.Argument(parser=get_module, default_factory=module_default_factory),
    ],
    out_dir: Annotated[Path, typer.Argument(file_okay=False)] = Path("temp"),
):
    # g = groupby(enumerate_modules(m, m.__package__), key=lambda x: x.path)

    d: dict[Path, list[MemberInfo]] = {}

    for current_module in modules:
        for member_info in enumerate_modules(
            current_module, current_module.__package__
        ):
            stub_path = member_info.path
            current_list = d.get(stub_path)
            if current_list is None:
                current_list = d[stub_path] = []
            current_list.append(member_info)

    import_header = """import os
from collections.abc import Callable
from typing import List

import osgeo.gdal
from osgeo import gdal"""

    for stub_path, member_infos in d.items():
        stub_path = out_dir / stub_path
        # Create the parent directory if it does not already exist
        stub_path.parent.mkdir(parents=True, exist_ok=True)
        # Open the file and write to it.
        print(f"Writing {stub_path}")
        with stub_path.open("wt+") as f:
            print(import_header, "\n", sep="\n", file=f)
            for mi in member_infos:
                text = format_value(mi.value, mi.name)
                print(text, file=f)


if __name__ == "__main__":
    _APP()
