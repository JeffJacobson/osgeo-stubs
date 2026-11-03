import os
from collections.abc import Callable
from typing import List

import osgeo.gdal
from osgeo import gdal

def create_metadata_file(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    overwrite: bool | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Create the _metadata file for a partitioned Parquet dataset

    Consult https://gdal.org/programs/gdal_driver_parquet_create_metadata_file.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input Parquet datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output Parquet dataset
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output Parquet dataset


    """
    ...
