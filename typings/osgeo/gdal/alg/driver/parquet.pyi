# typings\osgeo\gdal\alg\driver\parquet.pyi
import osgeo.gdal
import os
from collections.abc import Callable


def create_metadata_file(input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: osgeo.gdal.Dataset | str | os.PathLike[str], overwrite: bool | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Create the _metadata file for a partitioned Parquet dataset

       Consult https://gdal.org/programs/gdal_driver_parquet_create_metadata_file.html for more details.

       Parameters
       ----------
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
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

 


