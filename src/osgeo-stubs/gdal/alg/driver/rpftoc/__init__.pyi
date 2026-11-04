import os
from collections.abc import Callable
from typing import List

import osgeo.gdal
from osgeo import gdal


def create(input: str | os.PathLike[str], output: str | None = None, scale: int | None = None, producer_id: str | None = None, producer_name: str | None = None, country_code: str | None = None, classification: str | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Create a A.TOC index from CADRG frames.

       Consult https://gdal.org/drivers/raster/rpftoc.html for more details.

       Parameters
       ----------
       input: Union[str, os.PathLike[str]]
           Input directory
       output: Optional[str]=None
           Output filename
       scale: Optional[int]=None
           (Reciprocal) scale (e.g. 1000000)
       producer_id: Optional[str]=None
           Producer (short) identification
       producer_name: Optional[str]=None
           Producer name
       country_code: Optional[str]=None
           ISO country code for security
       classification: Optional[str]=None
           Index classification
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------


    """
    ...


