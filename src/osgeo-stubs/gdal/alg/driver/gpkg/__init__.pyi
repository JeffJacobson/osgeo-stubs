import os
from collections.abc import Callable
from typing import List

import osgeo.gdal
from osgeo import gdal


def repack(dataset: osgeo.gdal.Dataset | str | os.PathLike[str], progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Repack/vacuum in-place a GeoPackage dataset

       Consult https://gdal.org/programs/gdal_driver_gpkg_repack.html for more details.

       Parameters
       ----------
       dataset: Union[gdal.Dataset, str, os.PathLike[str]]
           GeoPackage dataset
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------


    """
    ...


def validate(dataset: osgeo.gdal.Dataset | str | os.PathLike[str], full_check: bool | None = None, verbose: bool | None = None, quiet: bool | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> str:
    """Validate conformance of a GeoPackage dataset against the GeoPackage specification

       Consult https://gdal.org/programs/gdal_driver_gpkg_validate.html for more details.

       Parameters
       ----------
       dataset: Union[gdal.Dataset, str, os.PathLike[str]]
           GeoPackage dataset
       full_check: Optional[bool]=None
           Whether to perform full check
       verbose: Optional[bool]=None
           Turn on verbose mode
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------
       output_string: str
           Output string, in which the result is placed


    """
    ...


