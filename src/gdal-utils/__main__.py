
import typer

from .constants import _APP as constants_app
from .dump import _APP as dump_app

_APP = typer.Typer()

_APP.add_typer(constants_app)
_APP.add_typer(dump_app)

if __name__ == "__main__":
    _APP()