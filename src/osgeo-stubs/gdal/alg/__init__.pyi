# typings\osgeo\gdal\alg.pyi
import osgeo.gdal
import os
from collections.abc import Callable

from . import dataset, mdim, raster, vector, vsi, driver

def pipeline(pipeline: str, quiet: bool | None = None, input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]] | None = None, output: osgeo.gdal.Dataset | str | os.PathLike[str] | None = None, output_format: str | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Process a dataset applying several steps.

       Consult https://gdal.org/programs/gdal_pipeline.html for more details.

       Parameters
       ----------
       pipeline: str
           Pipeline string or filename
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       input: Optional[Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]]=None
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

 


