import dataclasses
import re
from collections.abc import Generator
from types import ModuleType
from typing import Annotated, Any, Literal

import typer
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table

from . import enumerate_modules, get_module
from .dump import module_default_factory

_APP = typer.Typer()


@dataclasses.dataclass(order=True)
class ConstantInfo:
    module_name: str
    prefix: str | None
    member_name: str
    member_value: str

    def as_markdown_dict(self):
        return {
            "module": f"`{self.module_name}`",
            "prefix": f"`{self.prefix}`",
            "name": f"`{self.member_name}`",
            "value": f"`{self.member_value}`",
        }

    @staticmethod
    def group_by_name(items: list["ConstantInfo"]):
        pass

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


def enumerate_constants(
    *modules: ModuleType,
) -> Generator[ConstantInfo, Any, None]:
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

    if not format:
        table = Table("module", "prefix", "name", "value", title="Constants")

        for const_info in const_infos:
            table.add_row(*dataclasses.astuple(const_info))

        with Console() as c, c.pager(styles=True, links=True):
            c.print(table)
        return

    import pandas as pd

    if format == "markdown":
        const_infos = (c.as_markdown_dict() for c in const_infos)
        df = pd.DataFrame([*const_infos])
        with Console() as c:
            with c.capture() as cap:
                df.to_markdown(c.file, index=False)
            md = Markdown(cap.get())
            c.print(md)
