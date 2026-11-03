# typings\osgeo\gdal\alg\raster\overview.pyi
import osgeo.gdal
import os
from collections.abc import Callable


def add(quiet: bool | None = None, open_option: list[str] | dict | str | None = None, input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]] | None = None, overview_src: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]] | None = None, external: bool | None = None, resampling: str | None = None, levels: list[int] | int | None = None, min_size: int | None = None, creation_option: list[str] | dict | str | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Adding overviews.

       Consult https://gdal.org/programs/gdal_raster_overview_add.html for more details.

       Parameters
       ----------
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Aliases: dataset
           Dataset (to be updated in-place, unless --external)
       overview_src: Optional[Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]]=None
           Source overview dataset
       external: Optional[bool]=None
           Add external overviews
       resampling: Optional[str]=None
           Resampling method
       levels: Optional[Union[list[int], int]]=None
           Levels / decimation factors
       min_size: Optional[int]=None
           Maximum width or height of the smallest overview level.
       creation_option: Optional[Union[list[str], dict, str]]=None
           Overview creation option
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------


    """
    ...

 


def delete(quiet: bool | None = None, open_option: list[str] | dict | str | None = None, input: osgeo.gdal.Dataset | str | os.PathLike[str] | None = None, external: bool | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Deleting overviews.

       Consult https://gdal.org/programs/gdal_raster_overview_delete.html for more details.

       Parameters
       ----------
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       input: Union[gdal.Dataset, str, os.PathLike[str]]
           Aliases: dataset
           Dataset (to be updated in-place, unless --external)
       external: Optional[bool]=None
           Delete external overviews
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------


    """
    ...

 


def refresh(quiet: bool | None = None, open_option: list[str] | dict | str | None = None, input: osgeo.gdal.Dataset | str | os.PathLike[str] | None = None, external: bool | None = None, resampling: str | None = None, levels: list[int] | int | None = None, bbox: list[float] | float | None = None, like: list[str] | dict | str | None = None, use_source_timestamp: bool | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Refresh overviews.

       Consult https://gdal.org/programs/gdal_raster_overview_refresh.html for more details.

       Parameters
       ----------
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       input: Union[gdal.Dataset, str, os.PathLike[str]]
           Aliases: dataset
           Dataset (to be updated in-place, unless --external)
       external: Optional[bool]=None
           Refresh external overviews
       resampling: Optional[str]=None
           Resampling method
       levels: Optional[Union[list[int], int]]=None
           Levels / decimation factors
       bbox: Optional[Union[list[float], float]]=None
           Bounding box to refresh
       like: Optional[Union[list[str], dict, str]]=None
           Use extent of dataset(s)
       use_source_timestamp: Optional[bool]=None
           Use timestamp of VRT or GTI sources as refresh criterion
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------


    """
    ...

 


