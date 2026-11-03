# typings\osgeo\gdal\alg\mdim.pyi
import osgeo.gdal
import os
from collections.abc import Callable


def convert(input: osgeo.gdal.Dataset | str | os.PathLike[str], output: osgeo.gdal.Dataset | str | os.PathLike[str], quiet: bool | None = None, output_format: str | None = None, open_option: list[str] | dict | str | None = None, input_format: list[str] | dict | str | None = None, creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, array: list[str] | dict | str | None = None, array_option: list[str] | dict | str | None = None, group: list[str] | dict | str | None = None, subset: list[str] | dict | str | None = None, scale_axes: list[str] | dict | str | None = None, strict: bool | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Convert a multidimensional dataset.

       Consult https://gdal.org/programs/gdal_mdim_convert.html for more details.

       Parameters
       ----------
       input: Union[gdal.Dataset, str, os.PathLike[str]]
           Input raster or multidimensional raster dataset
       output: Union[gdal.Dataset, str, os.PathLike[str]]
           Output multidimensional raster dataset
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       output_format: Optional[str]=None
           Aliases: format
           Output format
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       creation_option: Optional[Union[list[str], dict, str]]=None
           Creation option
       overwrite: Optional[bool]=None
           Whether overwriting existing output dataset is allowed
       array: Optional[Union[list[str], dict, str]]=None
           Select a single array instead of converting the whole dataset.
       array_option: Optional[Union[list[str], dict, str]]=None
           Option passed to GDALGroup::GetMDArrayNames() to filter arrays.
       group: Optional[Union[list[str], dict, str]]=None
           Select a single group instead of converting the whole dataset.
       subset: Optional[Union[list[str], dict, str]]=None
           Select a subset of the data.
       scale_axes: Optional[Union[list[str], dict, str]]=None
           Applies a integral scale factor to one or several dimensions
       strict: Optional[bool]=None
           Turn warnings into failures.
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------
       output: gdal.ArgDatasetValue
           Output multidimensional raster dataset


    """
    ...

 


def info(open_option: list[str] | dict | str | None = None, input_format: list[str] | dict | str | None = None, input: osgeo.gdal.Dataset | str | os.PathLike[str] | None = None, summary: bool | None = None, detailed: bool | None = None, array: str | None = None, limit: int | None = None, array_option: list[str] | dict | str | None = None, stats: bool | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Return information on a multidimensional dataset.

       Consult https://gdal.org/programs/gdal_mdim_info.html for more details.

       Parameters
       ----------
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       input: Union[gdal.Dataset, str, os.PathLike[str]]
           Aliases: dataset
           Input multidimensional raster dataset
       summary: Optional[bool]=None
           Report only group and array hierarchy, without detailed information on attributes or dimensions.
       detailed: Optional[bool]=None
           Most verbose output. Report attribute data types and array values.
       array: Optional[str]=None
           Name of the array, used to restrict the output to the specified array.
       limit: Optional[int]=None
           Number of values in each dimension that is used to limit the display of array values.
       array_option: Optional[Union[list[str], dict, str]]=None
           Option passed to GDALGroup::GetMDArrayNames() to filter reported arrays.
       stats: Optional[bool]=None
           Read and display image statistics.
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------
       output_string: str
           Output string, in which the result is placed


    """
    ...

 


def mosaic(input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: osgeo.gdal.Dataset | str | os.PathLike[str], quiet: bool | None = None, output_format: str | None = None, open_option: list[str] | dict | str | None = None, input_format: list[str] | dict | str | None = None, creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, array: list[str] | dict | str | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Build a mosaic, either virtual (VRT) or materialized, from multidimensional datasets.

       Consult https://gdal.org/programs/gdal_mdim_mosaic.html for more details.

       Parameters
       ----------
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Input multidimensional raster datasets
       output: Union[gdal.Dataset, str, os.PathLike[str]]
           Output multidimensional raster dataset
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       output_format: Optional[str]=None
           Aliases: format
           Output format
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       creation_option: Optional[Union[list[str], dict, str]]=None
           Creation option
       overwrite: Optional[bool]=None
           Whether overwriting existing output dataset is allowed
       array: Optional[Union[list[str], dict, str]]=None
           Name of array(s) to mosaic.
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------
       output: gdal.ArgDatasetValue
           Output multidimensional raster dataset


    """
    ...

 


