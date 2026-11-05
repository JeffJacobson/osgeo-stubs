"""This script is a work in progress for, when it is finished,
will generate osgeo package type stubs.

Currently, the output needs to be further modified,
and files renamed and moved.

This would go beyond what alg_types.py does, also working with osgeo.
"""

import dataclasses
import importlib
import inspect
import re
from collections.abc import Callable, Generator
from pathlib import Path
from types import ModuleType
from typing import Annotated, Any, NamedTuple, cast

import typer
from rich.console import Console
from rich.table import Table

_APP = typer.Typer()


def predicate(value: Any) -> bool:
    """Determines if a member of a module should be returned from `inspect.getmembers`."""

    # To avoid recursion errors, only yield modules that do not have a __package__ value.
    if inspect.ismodule(value):
        if value.__package__ is not None:
            return False
    # Exclude anything with a name starting with either an underscore or "wrapper".
    elif (
        hasattr(value, "__name__")
        and isinstance(value.__name__, str)
        # and (value.__name__.startswith("_") or value.__name__.startswith("wrapper"))
        and any(value.__name__.startswith(n) for n in ["_", "wrapper"])
    ):
        return False

    # If it's reached this point then it can be included.
    return True


def find_output_type_in_doc(s: str):
    """
    >>> s = '''
    ... Output parameters
    ... -----------------
    ... output: gdal.ArgDatasetValue
    ...     Output vector dataset
    ... '''
    >>> t = find_output_type_in_doc(s)
    >>> print(t)
    gdal.ArgDatasetValue
    >>> s = '''
    ...    Output parameters
    ...    -----------------
    ...    return_code: int
    ...        Return code
    ... '''
    >>> t = find_output_type_in_doc(s)
    >>> print(t)
    int
    """

    # TODO: Handle multiple outputs
    #    Output parameters
    #    -----------------
    #    output: gdal.ArgDatasetValue
    #        Output vector dataset
    #    output_string: str
    #        Output string, in which the result is placed

    pattern = re.compile(r"\s*Output parameters\n\s*-+\n\s*\w+: (?P<type>\S+)")
    m = pattern.search(s)
    if not m:
        return None
    else:
        output = m[1]
        output = cast(str, output)
        return output


def format_callable(c: Callable) -> str:
    """Write type stub for a callable.

    TODO: The signatures of the osgeo functions (except for the osgeo.gdal.alg)
    do not have type definitions. However their docstrings DO list the types
    (but sometimes C++ types rather than Python types).

    We need to:
    * Detect if the docstring contains a signature. (Not all do.)
    * Extract the signatures in the docstring
    * Convert the C++ types to Python types. (e.g., `char const *` to `str`)
    """

    # Initialize output string with "..." (unknown)
    return_type_string = "..."
    signature = inspect.signature(c)
    name = c.__name__
    doc = c.__doc__
    # Replace if a return time is in the signature.
    if not signature.empty:
        return_type_string = signature.return_annotation
    elif re.search(r"\bgdal\.alg\b", c.__module__):
        return_type_string = "gdal.Algorithm"
    # If we haven't determined the output type yet, try to extract it from the docstring
    if return_type_string == "..." and doc:
        extracted_output_type = find_output_type_in_doc(doc)
        if extracted_output_type:
            return_type_string = extracted_output_type

    current_text = f'''def {name}{signature} -> {return_type_string}:
    """{doc}
    """
    ...

'''

    return current_text


def format_class(value: type[Any]):
    # class_members = inspect.getmembers_static(value)

    # def indent_lines(s: str, indent: int):
    #     lines = s.splitlines()

    # formatted_members = (
    #     format_value(current_value, current_name)
    #     for current_name, current_value in class_members:
    #         pass
    # )

    raise NotImplementedError()


def format_value(value: Any, name: str) -> str:
    if inspect.isclass(value):
        # return format_class(value)
        pass
    elif callable(value):
        return format_callable(value)
    elif isinstance(value, int | str | bool):
        return f"{name}: Literal[{repr(value)}]"
    elif isinstance(value, float):
        return f"{name} = {repr(value)}"
    return f"# {repr(value)}"


class MemberInfoRenderables(NamedTuple):
    path: str
    package: str
    module: str
    type: str
    name: str
    value: str


@dataclasses.dataclass()
class MemberInfo:
    """Represents information about a module member."""

    path: Path
    package: str | None
    module: ModuleType
    name: str
    value: Any

    def as_renderables(self):
        """Returns properties as a tuple of values that are
        renderable by a `rich.tables.Table`.
        """
        return MemberInfoRenderables(
            str(self.path.as_posix()),
            repr(self.package) if self.package is None else self.package,
            self.module.__name__,
            repr(type(self.value)),
            self.name,
            format_value(self.value, self.name),
        )


def enumerate_modules(
    module: ModuleType,
    package: str | None = None,
) -> Generator[MemberInfo]:
    for name, value in inspect.getmembers(
        module,
        predicate=predicate,
    ):
        if any(name.startswith(v) for v in ["_", "wrapper"]):
            continue
        if inspect.ismodule(value):
            yield from enumerate_modules(value, package)
        else:
            path = module.__name__.split(".")
            if path[0] != "osgeo":
                path = ["osgeo", *path]
            path = Path(*path) / "__init__.pyi"
            yield MemberInfo(path, package, module, name, value)


def get_module(module_name: str):
    """Gets the named module.
    Used by typer, because it can't handle ModuleType by default

    Args:
        module_name: the name of a module

    Returns:
        The module corresponding to the module name.
    """
    return importlib.import_module(module_name)

    # # TODO: For dynamic modules like osgeo.gdal.alg that can't be imported via importlib,
    # # import the first importable parent, then return the module from there.
    # name_parts = module_name.split(".")
    # failed_parts: list[str] = []
    # the_module: ModuleType | None = None
    # while not the_module or name_parts:
    #     try:
    #         the_module = importlib.import_module(module_name)
    #     except ImportError as ierr:
    #         failed_parts.append(name_parts.pop())
    #         module_name = ".".join(name_parts)

    # return the_module


def module_default_factory():
    """Sets the default modules if user omits them

    Returns:
        A list of strings, which are the names of modules
    """
    return [
        f"osgeo.{n}" for n in ["gdal", "gdalconst", "ogr", "osr", "gdal_array", "gnm"]
    ]
    # return ["osgeo.gdal", "osgeo.gdalconst", "osgeo.ogr", "osgeo.osr"]


class EnumerateConstantsTuple(NamedTuple):
    module_name: str
    prefix: str | None
    member_name: str
    member_value: str


def enumerate_constants(
    *modules: ModuleType,
) -> Generator[EnumerateConstantsTuple, Any, None]:
    """Enumerates info tuples about the constants in the given modules.

    Yields:
        _description_
    """

    # List of prefixes that consist of more than one part (separated by underscores)
    prefixes = [
        "ALTER",
        "CE",
        "CPLE",
        "CPLES",
        "CXT",
        "DCAP",
        "DIM_TYPE",
        "DMD",
        "F_VAL",
        "GA",
        "GAAT",
        "GADV",
        "GARIO",
        "GAT",
        "GCI",
        "GDAL_DATA_COVERAGE",
        "GDAL_DCAP",
        "GDAL_DMD",
        "GDT",
        "GDsC",
        "GEDTC",
        "GEDTST",
        "GEOS_PREC",
        "GF",
        "GFT",
        "GFU",
        "GGT",
        "GMF",
        "GNM_EDGE_DIR",
        "GPI",
        "GRA",
        "GRABO",
        "GRAUO",
        "GRC",
        "GRIORA",
        "GRT",
        "GRTT",
        "GTO",
        "GVM",
        "GVOT",
        "OAMS",
        "OAO",
        "ODrC",
        "ODsC",
        "OF",
        "OFDMP",
        "OFDSP",
        "OFDT",
        "OFST",
        "OFT",
        "OGRERR",
        "OJ",
        "OLC",
        "OLMD",
        "OSR_CRS_TYPE",
        "PROJ_ERR",
        "SRS",
        "SRS_DN",
        "SRS_PP",
        "SRS_PT",
        "SRS_UA",
        "SRS_UL",
        "SRS_WGS84",
        "SRS_WKT",
        "TZFLAG",
        "VSI",
        "wkb",
    ]

    const_name_pattern = re.compile(r"^(?P<prefix>[A-Z][A-Z0-9]+)_\w+$")

    def get_prefix(s: str):
        for p in prefixes:
            if s.startswith(p):
                return p
        if const_name_pattern.match(s):
            return mi.name.split("_", 1)[0]
        return None

    # # This was used to generate the list of prefixes. Won't be needed unless GDAL adds more constants.
    # found_prefixes = set(prefixes)
    for module in modules:
        member_infos = [
            mi
            for mi in enumerate_modules(module)
            if isinstance(mi.value, str | bool | int | float)
            # and const_name_pattern.match(mi.name)
        ]
        member_infos.sort(key=lambda x: x.name)
        for mi in member_infos:
            prefix = get_prefix(mi.name)
            yield EnumerateConstantsTuple(
                mi.module.__name__, prefix, mi.name, repr(mi.value)
            )

            # if prefix:
            #     found_prefixes.add(prefix)


@_APP.command("consts")
def list_consts(
    modules: Annotated[
        list[ModuleType],
        typer.Argument(parser=get_module, default_factory=module_default_factory),
    ],
    # format: Annotated[str | None, typer.Option()] = None,
):
    table = Table("module", "prefix", "name", "value", title="Constants")

    for const_info in enumerate_constants(*modules):
        table.add_row(*const_info)

    with Console() as c, c.pager(styles=True, links=True):
        c.print(table)
        # c.print(sorted(found_prefixes))


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
