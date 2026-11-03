# typings\osgeo\gdal\alg\vsi.pyi
import osgeo.gdal
import os
from collections.abc import Callable


def sync(source: str, destination: str, quiet: bool | None = None, recursive: bool | None = None, strategy: str | None = None, num_threads: str | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Synchronize source and target file/directory located on GDAL Virtual System Interface (VSI).

       Consult https://gdal.org/programs/gdal_vsi_sync.html for more details.

       Parameters
       ----------
       source: str
           Source file or directory name
       destination: str
           Destination file or directory name
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       recursive: Optional[bool]=None
           Synchronize recursively
       strategy: Optional[str]=None
           Synchronization strategy
       num_threads: Optional[str]=None
           Number of jobs (or ALL_CPUS)
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------


    """
    ...

 


