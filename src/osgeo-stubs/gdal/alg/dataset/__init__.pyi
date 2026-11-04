import os
from collections.abc import Callable
from typing import List

import osgeo.gdal
from osgeo import gdal


def check(input: osgeo.gdal.Dataset | str | os.PathLike[str], quiet: bool | None = None, open_option: List[str] | dict | str | None = None, input_format: List[str] | dict | str | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> int:
    """Check whether there are errors when reading the content of a dataset.

       Consult https://gdal.org/programs/gdal_dataset_check.html for more details.

       Parameters
       ----------
       input: Union[gdal.Dataset, str, os.PathLike[str]]
           Input raster, vector or multidimensional raster dataset
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       open_option: Optional[Union[List[str], dict, str]]=None
           Open options
       input_format: Optional[Union[List[str], dict, str]]=None
           Input formats
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------
       return_code: int
           Return code


    """
    ...


def copy(source: str, destination: str, overwrite: bool | None = None, format: str | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Copy files of a dataset.

       Consult https://gdal.org/programs/gdal_dataset_copy.html for more details.

       Parameters
       ----------
       source: str
           Source dataset name
       destination: str
           Destination dataset name
       overwrite: Optional[bool]=None
           Whether overwriting existing output dataset is allowed
       format: Optional[str]=None
           Dataset format
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------


    """
    ...


def delete(filename: List[str] | dict | str, format: str | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Delete dataset(s).

       Consult https://gdal.org/programs/gdal_dataset_delete.html for more details.

       Parameters
       ----------
       filename: Union[List[str], dict, str]
           File or directory name
       format: Optional[str]=None
           Dataset format
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------


    """
    ...


def identify(quiet: bool | None = None, filename: List[str] | dict | str | None = None, output: osgeo.gdal.Dataset | str | os.PathLike[str] | None = None, output_format: str | None = None, creation_option: List[str] | dict | str | None = None, layer_creation_option: List[str] | dict | str | None = None, output_layer: str | None = None, overwrite: bool | None = None, recursive: bool | None = None, force_recursive: bool | None = None, detailed: bool | None = None, report_failures: bool | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> gdal.ArgDatasetValue:
    """Identify driver opening dataset(s).

       Consult https://gdal.org/programs/gdal_dataset_identify.html for more details.

       Parameters
       ----------
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       filename: Union[List[str], dict, str]
           Aliases: input
           File or directory name
       output: Optional[Union[gdal.Dataset, str, os.PathLike[str]]]=None
           Output vector dataset
       output_format: Optional[str]=None
           Aliases: format
           Output format
       creation_option: Optional[Union[List[str], dict, str]]=None
           Creation option
       layer_creation_option: Optional[Union[List[str], dict, str]]=None
           Layer creation option
       output_layer: Optional[str]=None
           Output layer name
       overwrite: Optional[bool]=None
           Whether overwriting existing output dataset is allowed
       recursive: Optional[bool]=None
           Recursively scan files/folders for datasets
       force_recursive: Optional[bool]=None
           Recursively scan folders for datasets, forcing recursion in folders recognized as valid formats
       detailed: Optional[bool]=None
           Most detailed output. Reports the presence of georeferencing, if a GeoTIFF file is cloud optimized, etc.
       report_failures: Optional[bool]=None
           Report failures if file type is unidentified
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------
       output: gdal.ArgDatasetValue
           Output vector dataset
       output_string: str
           Output string, in which the result is placed


    """
    ...


def rename(source: str, destination: str, overwrite: bool | None = None, format: str | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Rename files of a dataset.

       Consult https://gdal.org/programs/gdal_dataset_rename.html for more details.

       Parameters
       ----------
       source: str
           Source dataset name
       destination: str
           Destination dataset name
       overwrite: Optional[bool]=None
           Whether overwriting existing output dataset is allowed
       format: Optional[str]=None
           Dataset format
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------


    """
    ...


