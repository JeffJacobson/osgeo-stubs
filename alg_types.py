"""Generate type stubs for osgeo.gdal.alg"""

import enum
import importlib
import inspect
import re
from collections.abc import Generator
from itertools import groupby
from pathlib import Path
from types import ModuleType
from typing import Annotated, NamedTuple

import typer
from rich.console import Console
from rich.progress import track
from rich.table import Table


class MemberType(enum.Enum):
    CALLABLE = "CALLABLE"
    MODULE = "MODULE"
    OTHER = "OTHER"


class InfoTuple(NamedTuple):
    """A tuple of information about a module member.

    Arguments:
        pyi_path:
            Path for this member's `.pyi` file.
        member_type:
            Indicates what type of member this is.

            * "CALLABLE"
            * "MODULE"
            * "OTHER"
        name:
            The name of the member.
        signature (inspect.Signature | None | type):
            The member's signature or type

        docstring: The member's docstring
    """

    pyi_path: Path
    member_type: MemberType
    name: str
    signature: inspect.Signature | None | type
    docstring: str | None


def walk(obj: ModuleType) -> Generator[InfoTuple]:
    """Iterate the members of the given module.

    Args:
        obj: The module
        prefix: A prefix to be appended to the output. Defaults to "".

    Yields:
        An `InfoTuple`
    """
    for name, member in inspect.getmembers(obj):
        # Skip names starting with "_", which is Python
        # convention for a private member.
        if name.startswith("_"):
            continue

        # Construct the output file path for this module by splitting this
        # name at the periods for args of Path, then adding the ".pyi" suffix.
        pyi_path = Path(*obj.__name__.split(".")).with_suffix(".pyi")

        # If the current member is a module, recursively walk its members.
        if inspect.ismodule(member):
            yield from walk(member)
        else:
            # Yield member information
            if callable(member):
                yield InfoTuple(
                    pyi_path=pyi_path,
                    member_type=MemberType.CALLABLE,
                    name=name,
                    signature=inspect.signature(member) if callable(member) else None,
                    docstring=member.__doc__,
                )
            else:
                yield InfoTuple(
                    pyi_path, MemberType.OTHER, name, type(member), member.__doc__
                )


_APP = typer.Typer()

_DEFAULT_OUT_DIR = Path(".") / "typings" / "osgeo"


@_APP.command()
def dump(out_dir: Annotated[Path, typer.Option()] = _DEFAULT_OUT_DIR):
    """Creates Python type stubs for gdal.alg"""

    # Create a variable for the module
    the_module = importlib.import_module("osgeo.gdal")

    the_module: ModuleType = the_module.alg

    # Iterate the module
    grouped_items = groupby(walk(the_module), lambda i: i[0])
    grouped_items = {g: [*v] for g, v in grouped_items}

    table_field_names = [
        "Group #",
        "pyi_path",
        "name",
        "member_type",
        # "signature",
        # "docstring",
    ]
    table = Table(*table_field_names, title=f"Members of {the_module.__name__}")

    for i, (pyi_path, info_tuples) in track(enumerate(grouped_items.items())):
        pyi_path = out_dir / pyi_path
        pyi_path.parent.mkdir(parents=True, exist_ok=True)
        if i > 0:
            table.add_section()
        with pyi_path.open("w+t", encoding="utf-8") as f:
            print(
                f"# {pyi_path}",
                "import osgeo.gdal",
                "import os",
                "from collections.abc import Callable",
                "\n",
                sep="\n",
                file=f,
            )

            for current_info in info_tuples:
                _module, member_type, name, signature, doc = current_info
                if member_type == MemberType.CALLABLE:
                    # Initialize output string with "..." (unknown)
                    return_type_string = "..."
                    # Replace if a return time is in the signature.
                    if isinstance(signature, inspect.Signature) and not signature.empty:
                        return_type_string = signature.return_annotation
                    current_text = f'''def {name}{signature} -> {return_type_string}:
    """{doc}
    """
    ...

'''
                    current_text = "list".join(re.split(r"\bList\b", current_text))

                    print(current_text, "\n" * 2, file=f)
                    # print(
                    #     f"def {qualified_name}{signature} -> {return_type_string}:",
                    #     f'"""{doc}"""',
                    #     "...",
                    #     "\n",
                    #     sep="\n    ",
                    #     file=f,
                    # )
                elif member_type == "OTHER":
                    pass
                table.add_row(f"{i}", name, member_type.name, f"{pyi_path}")

    with Console() as console:
        console.print(table)


if __name__ == "__main__":
    _APP()
