# typings\osgeo\gdal\alg\driver\cog.pyi
import osgeo.gdal
import os
from collections.abc import Callable


def validate(dataset: osgeo.gdal.Dataset | str | os.PathLike[str] | None = None, full_check: str | None = None, quiet: bool | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Validate if a TIFF file is a Cloud Optimized GeoTIFF

       Consult https://gdal.org/programs/gdal_driver_cog_validate.html for more details.

       Parameters
       ----------
       dataset: Union[gdal.Dataset, str, os.PathLike[str]]
           Aliases: input
           COG dataset
       full_check: Optional[str]=None
           Whether to perform full check
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

 


