import os
from collections.abc import Callable
from typing import List

import osgeo.gdal
from osgeo import gdal

from . import dataset, driver, mdim, raster, vector, vsi

__all__ = ["dataset", "driver", "mdim", "raster", "vector", "vsi"]

def convert(
    input: osgeo.gdal.Dataset | str | os.PathLike[str],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    quiet: bool | None = None,
    output_format: str | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Convert a dataset (shortcut for 'gdal raster convert' or 'gdal vector convert').

    Consult https://gdal.org/programs/gdal_convert.html for more details.

    Parameters
    ----------
    input: Union[gdal.Dataset, str, os.PathLike[str]]
        Input raster, vector or multidimensional raster dataset
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster, vector or multidimensional raster dataset
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster, vector or multidimensional raster dataset


    """
    ...

def info(
    output_format: str | None = None,
    input: osgeo.gdal.Dataset | str | os.PathLike[str] | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Return information on a dataset (shortcut for 'gdal raster info' or 'gdal vector info').

    Consult https://gdal.org/programs/gdal_info.html for more details.

    Parameters
    ----------
    output_format: Optional[str]=None
        Aliases: format
        Output format
    input: Union[gdal.Dataset, str, os.PathLike[str]]
        Aliases: dataset
        Input raster, vector or multidimensional raster dataset
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------


    """
    ...

def pipeline(
    pipeline: str,
    quiet: bool | None = None,
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]] | None = None,
    output: osgeo.gdal.Dataset | str | os.PathLike[str] | None = None,
    output_format: str | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Process a dataset applying several steps.

    Consult https://gdal.org/programs/gdal_pipeline.html for more details.

    Parameters
    ----------
    pipeline: str
        Pipeline string or filename
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    input: Optional[Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]]=None
        Input raster or vector datasets
    output: Optional[Union[gdal.Dataset, str, os.PathLike[str]]]=None
        Output raster or vector dataset
    output_format: Optional[str]=None
        Aliases: format
        Output format ("GDALG" allowed)
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster or vector dataset
    output_string: str
        Output string, in which the result is placed


    """
    ...
