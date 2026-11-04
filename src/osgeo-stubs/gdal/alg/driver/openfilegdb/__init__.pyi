import os
from collections.abc import Callable
from typing import List

import osgeo.gdal
from osgeo import gdal


def repack(dataset: osgeo.gdal.Dataset | str | os.PathLike[str], quiet: bool | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Repack a FileGeoDatabase dataset

       Consult https://gdal.org/drivers/vector/openfilegdb.html for more details.

       Parameters
       ----------
       dataset: Union[gdal.Dataset, str, os.PathLike[str]]
           FileGeoDatabase dataset
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------


    """
    ...


