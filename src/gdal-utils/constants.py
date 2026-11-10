import dataclasses
import re
from collections.abc import Generator, Sequence
from types import ModuleType
from typing import Annotated, Any, Literal, cast, overload

import typer
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table

from . import enumerate_modules, get_module
from .dump import module_default_factory

_APP = typer.Typer()


type OsgeoConstPrefix = Literal[
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

# List of prefixes that consist of more than one part (separated by underscores)
const_prefixes: tuple[OsgeoConstPrefix, ...] = (
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
)


@dataclasses.dataclass(order=True)
class ConstantInfo:
    module_name: str
    prefix: OsgeoConstPrefix
    member_name: str
    member_value: str | int | float

    def as_markdown_dict(self):
        return {
            "module": f"`{self.module_name}`",
            "prefix": f"`{self.prefix}`",
            "name": f"`{self.member_name}`",
            "value": f"`{self.member_value}`",
        }

    def as_tuple(self):
        return (self.module_name, self.prefix, self.member_name, self.member_value)

    # @staticmethod
    # def as_markdown_table(*items: "ConstantInfo"):
    #     import pandas as pd

    #     df = pd.DataFrame(items)
    #     # sep = " | "
    #     # data_rows = (sep.join(dataclasses.astuple(item)) for item in items)
    #     # header_row = "\n".join(
    #     #     (sep.join(["Module", "Prefix", "Name", "Value"]), sep.join(("-",) * 4))
    #     # )
    #     # return "\n".join(header_row, *data_rows)


@dataclasses.dataclass(order=True)
class MultiModuleConstantInfo:
    module_names: set[str]
    prefix: OsgeoConstPrefix
    member_name: str
    member_value: str | int | float

    @staticmethod
    def from_const_info(ci: ConstantInfo):
        return MultiModuleConstantInfo(
            {ci.module_name}, ci.prefix, ci.member_name, ci.member_value
        )

    def as_markdown_dict(self):
        modules = "\n".join(self.module_names)
        return {
            "modules": modules,
            "prefix": f"`{self.prefix}`",
            "name": f"`{self.member_name}`",
            "value": f"`{self.member_value}`",
        }

    @staticmethod
    def to_dicts_with_one_column_per_module(
        items: Sequence["MultiModuleConstantInfo"], markdown: bool = False
    ):
        # Get a set of all of the possible module names
        # module_names = [item.module_names for item in items]
        module_names: set[str] = set()
        for item in items:
            for mn in item.module_names:
                module_names.add(mn)
        # For each item, yield its properties as a dict, with an additional
        # value for each module name indicating if the current item is in
        # that module.
        for item in items:
            hasses = dict(
                (mn, mn if mn in item.module_names else "") for mn in module_names
            )
            d = item.as_markdown_dict()
            del d["modules"]
            if item.member_name == "SRS_WKT_WGS84_LAT_LONG":
                d["value"] = "…"
            d = {**d, **hasses}
            yield d


@overload
def group_by_name(
    items: Sequence["ConstantInfo"], return_dict: Literal[False]
) -> tuple[MultiModuleConstantInfo]: ...
@overload
def group_by_name(
    items: Sequence["ConstantInfo"], return_dict: Literal[True] = True
) -> dict[str, MultiModuleConstantInfo]: ...
def group_by_name(items: Sequence["ConstantInfo"], return_dict: bool = True):
    """Return a collection where each constant is only represented once, even if it is in multiple modules."""
    output_dict: dict[str, MultiModuleConstantInfo] = {}

    for input_item in items:
        module, prefix, name, value = input_item.as_tuple()
        current_item = output_dict.get(name)
        if current_item:
            current_item.module_names.add(module)
        else:
            output_dict[name] = MultiModuleConstantInfo({module}, prefix, name, value)

    if return_dict:
        return output_dict

    return (*(v for _, v in output_dict.items()),)


def enumerate_constants(
    *modules: ModuleType,
) -> Generator[ConstantInfo, Any, None]:
    """Enumerates info tuples about the constants in the given modules.

    Yields:
        _description_
    """

    const_name_pattern = re.compile(r"^(?P<prefix>[A-Z][A-Z0-9]+)_\w+$")

    def get_prefix(s: str):
        for p in const_prefixes:
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
            prefix = cast(OsgeoConstPrefix, get_prefix(mi.name))
            yield ConstantInfo(mi.module.__name__, prefix, mi.name, repr(mi.value))

            # if prefix:
            #     found_prefixes.add(prefix)


@_APP.command("consts")
def list_consts(
    modules: Annotated[
        list[ModuleType],
        typer.Argument(
            parser=get_module,
            default_factory=module_default_factory,
            help=f"Defaults: {module_default_factory()}",
        ),
    ],
    format: Annotated[Literal["markdown"] | None, typer.Option()] = None,
):
    const_infos = enumerate_constants(*modules)
    const_infos = group_by_name([*const_infos], False)

    if not format:
        table = Table("prefix", "name", "value", "modules", title="Constants")

        # for const_info in const_infos:
        #     table.add_row(*dataclasses.astuple(const_info))

        for ci in const_infos:
            table.add_row(
                ci.prefix,
                ci.member_name,
                repr(ci.member_value),
                ",".join(ci.module_names),
            )

        with Console() as c, c.pager(styles=True, links=True):
            c.print(table)
        return

    import pandas as pd

    if format == "markdown":
        const_infos = MultiModuleConstantInfo.to_dicts_with_one_column_per_module(
            const_infos
        )
        df = pd.DataFrame([*const_infos])
        with Console() as c:
            with c.capture() as cap:
                df.to_markdown(c.file, index=False)
            md = Markdown(cap.get())
            c.print(md)
