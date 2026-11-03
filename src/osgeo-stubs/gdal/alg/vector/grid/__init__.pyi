import os
from collections.abc import Callable
from typing import List

import osgeo.gdal
from osgeo import gdal

def average(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    quiet: bool | None = None,
    output_format: str | None = None,
    open_option: List[str] | dict | str | None = None,
    input_format: List[str] | dict | str | None = None,
    creation_option: List[str] | dict | str | None = None,
    extent: List[float] | float | None = None,
    resolution: List[float] | float | None = None,
    size: List[int] | int | None = None,
    output_data_type: str | None = None,
    crs: str | None = None,
    overwrite: bool | None = None,
    input_layer: List[str] | dict | str | None = None,
    sql: str | None = None,
    bbox: List[float] | float | None = None,
    zfield: str | None = None,
    zoffset: float | None = None,
    zmultiply: float | None = None,
    radius: float | None = None,
    radius1: float | None = None,
    radius2: float | None = None,
    angle: float | None = None,
    min_points: int | None = None,
    max_points: int | None = None,
    min_points_per_quadrant: int | None = None,
    max_points_per_quadrant: int | None = None,
    nodata: float | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Create a regular grid from scattered points using moving average interpolation.

    Consult https://gdal.org/programs/gdal_vector_grid.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input vector datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    extent: Optional[Union[List[float], float]]=None
        Set the target georeferenced extent
    resolution: Optional[Union[List[float], float]]=None
        Set the target resolution
    size: Optional[Union[List[int], int]]=None
        Set the target size in pixels and lines
    output_data_type: Optional[str]=None
        Aliases: datatype
        Output data type
    crs: Optional[str]=None
        Override the projection for the output file
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    input_layer: Optional[Union[List[str], dict, str]]=None
        Aliases: layer
        Input layer name
    sql: Optional[str]=None
        SQL statement
    bbox: Optional[Union[List[float], float]]=None
        Select only points contained within the specified bounding box
    zfield: Optional[str]=None
        Field name from which to get Z values.
    zoffset: Optional[float]=None
        Value to add to the Z field value (applied before zmultiply)
    zmultiply: Optional[float]=None
        Multiplication factor for the Z field value (applied after zoffset)
    radius: Optional[float]=None
        Radius of the search circle
    radius1: Optional[float]=None
        First axis of the search ellipse
    radius2: Optional[float]=None
        Second axis of the search ellipse
    angle: Optional[float]=None
        Angle of search ellipse rotation in degrees (counter clockwise)
    min_points: Optional[int]=None
        Minimum number of data points to use
    max_points: Optional[int]=None
        Maximum number of data points to use
    min_points_per_quadrant: Optional[int]=None
        Minimum number of data points to use per quadrant
    max_points_per_quadrant: Optional[int]=None
        Maximum number of data points to use per quadrant
    nodata: Optional[float]=None
        Target nodata value
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def average_distance(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    quiet: bool | None = None,
    output_format: str | None = None,
    open_option: List[str] | dict | str | None = None,
    input_format: List[str] | dict | str | None = None,
    creation_option: List[str] | dict | str | None = None,
    extent: List[float] | float | None = None,
    resolution: List[float] | float | None = None,
    size: List[int] | int | None = None,
    output_data_type: str | None = None,
    crs: str | None = None,
    overwrite: bool | None = None,
    input_layer: List[str] | dict | str | None = None,
    sql: str | None = None,
    bbox: List[float] | float | None = None,
    zfield: str | None = None,
    zoffset: float | None = None,
    zmultiply: float | None = None,
    radius: float | None = None,
    radius1: float | None = None,
    radius2: float | None = None,
    angle: float | None = None,
    min_points: int | None = None,
    min_points_per_quadrant: int | None = None,
    max_points_per_quadrant: int | None = None,
    nodata: float | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Create a regular grid from scattered points using the average distance between the grid node (center of the search ellipse) and all of the data points in the search ellipse.

    Consult https://gdal.org/programs/gdal_vector_grid.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input vector datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    extent: Optional[Union[List[float], float]]=None
        Set the target georeferenced extent
    resolution: Optional[Union[List[float], float]]=None
        Set the target resolution
    size: Optional[Union[List[int], int]]=None
        Set the target size in pixels and lines
    output_data_type: Optional[str]=None
        Aliases: datatype
        Output data type
    crs: Optional[str]=None
        Override the projection for the output file
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    input_layer: Optional[Union[List[str], dict, str]]=None
        Aliases: layer
        Input layer name
    sql: Optional[str]=None
        SQL statement
    bbox: Optional[Union[List[float], float]]=None
        Select only points contained within the specified bounding box
    zfield: Optional[str]=None
        Field name from which to get Z values.
    zoffset: Optional[float]=None
        Value to add to the Z field value (applied before zmultiply)
    zmultiply: Optional[float]=None
        Multiplication factor for the Z field value (applied after zoffset)
    radius: Optional[float]=None
        Radius of the search circle
    radius1: Optional[float]=None
        First axis of the search ellipse
    radius2: Optional[float]=None
        Second axis of the search ellipse
    angle: Optional[float]=None
        Angle of search ellipse rotation in degrees (counter clockwise)
    min_points: Optional[int]=None
        Minimum number of data points to use
    min_points_per_quadrant: Optional[int]=None
        Minimum number of data points to use per quadrant
    max_points_per_quadrant: Optional[int]=None
        Maximum number of data points to use per quadrant
    nodata: Optional[float]=None
        Target nodata value
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def average_distance_points(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    quiet: bool | None = None,
    output_format: str | None = None,
    open_option: List[str] | dict | str | None = None,
    input_format: List[str] | dict | str | None = None,
    creation_option: List[str] | dict | str | None = None,
    extent: List[float] | float | None = None,
    resolution: List[float] | float | None = None,
    size: List[int] | int | None = None,
    output_data_type: str | None = None,
    crs: str | None = None,
    overwrite: bool | None = None,
    input_layer: List[str] | dict | str | None = None,
    sql: str | None = None,
    bbox: List[float] | float | None = None,
    zfield: str | None = None,
    zoffset: float | None = None,
    zmultiply: float | None = None,
    radius: float | None = None,
    radius1: float | None = None,
    radius2: float | None = None,
    angle: float | None = None,
    min_points: int | None = None,
    min_points_per_quadrant: int | None = None,
    max_points_per_quadrant: int | None = None,
    nodata: float | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Create a regular grid from scattered points using the average distance between the data points in the search ellipse.

    Consult https://gdal.org/programs/gdal_vector_grid.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input vector datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    extent: Optional[Union[List[float], float]]=None
        Set the target georeferenced extent
    resolution: Optional[Union[List[float], float]]=None
        Set the target resolution
    size: Optional[Union[List[int], int]]=None
        Set the target size in pixels and lines
    output_data_type: Optional[str]=None
        Aliases: datatype
        Output data type
    crs: Optional[str]=None
        Override the projection for the output file
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    input_layer: Optional[Union[List[str], dict, str]]=None
        Aliases: layer
        Input layer name
    sql: Optional[str]=None
        SQL statement
    bbox: Optional[Union[List[float], float]]=None
        Select only points contained within the specified bounding box
    zfield: Optional[str]=None
        Field name from which to get Z values.
    zoffset: Optional[float]=None
        Value to add to the Z field value (applied before zmultiply)
    zmultiply: Optional[float]=None
        Multiplication factor for the Z field value (applied after zoffset)
    radius: Optional[float]=None
        Radius of the search circle
    radius1: Optional[float]=None
        First axis of the search ellipse
    radius2: Optional[float]=None
        Second axis of the search ellipse
    angle: Optional[float]=None
        Angle of search ellipse rotation in degrees (counter clockwise)
    min_points: Optional[int]=None
        Minimum number of data points to use
    min_points_per_quadrant: Optional[int]=None
        Minimum number of data points to use per quadrant
    max_points_per_quadrant: Optional[int]=None
        Maximum number of data points to use per quadrant
    nodata: Optional[float]=None
        Target nodata value
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def count(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    quiet: bool | None = None,
    output_format: str | None = None,
    open_option: List[str] | dict | str | None = None,
    input_format: List[str] | dict | str | None = None,
    creation_option: List[str] | dict | str | None = None,
    extent: List[float] | float | None = None,
    resolution: List[float] | float | None = None,
    size: List[int] | int | None = None,
    output_data_type: str | None = None,
    crs: str | None = None,
    overwrite: bool | None = None,
    input_layer: List[str] | dict | str | None = None,
    sql: str | None = None,
    bbox: List[float] | float | None = None,
    zfield: str | None = None,
    zoffset: float | None = None,
    zmultiply: float | None = None,
    radius: float | None = None,
    radius1: float | None = None,
    radius2: float | None = None,
    angle: float | None = None,
    min_points: int | None = None,
    min_points_per_quadrant: int | None = None,
    max_points_per_quadrant: int | None = None,
    nodata: float | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Create a regular grid from scattered points using the number of points in the search ellipse.

    Consult https://gdal.org/programs/gdal_vector_grid.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input vector datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    extent: Optional[Union[List[float], float]]=None
        Set the target georeferenced extent
    resolution: Optional[Union[List[float], float]]=None
        Set the target resolution
    size: Optional[Union[List[int], int]]=None
        Set the target size in pixels and lines
    output_data_type: Optional[str]=None
        Aliases: datatype
        Output data type
    crs: Optional[str]=None
        Override the projection for the output file
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    input_layer: Optional[Union[List[str], dict, str]]=None
        Aliases: layer
        Input layer name
    sql: Optional[str]=None
        SQL statement
    bbox: Optional[Union[List[float], float]]=None
        Select only points contained within the specified bounding box
    zfield: Optional[str]=None
        Field name from which to get Z values.
    zoffset: Optional[float]=None
        Value to add to the Z field value (applied before zmultiply)
    zmultiply: Optional[float]=None
        Multiplication factor for the Z field value (applied after zoffset)
    radius: Optional[float]=None
        Radius of the search circle
    radius1: Optional[float]=None
        First axis of the search ellipse
    radius2: Optional[float]=None
        Second axis of the search ellipse
    angle: Optional[float]=None
        Angle of search ellipse rotation in degrees (counter clockwise)
    min_points: Optional[int]=None
        Minimum number of data points to use
    min_points_per_quadrant: Optional[int]=None
        Minimum number of data points to use per quadrant
    max_points_per_quadrant: Optional[int]=None
        Maximum number of data points to use per quadrant
    nodata: Optional[float]=None
        Target nodata value
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def invdist(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    quiet: bool | None = None,
    output_format: str | None = None,
    open_option: List[str] | dict | str | None = None,
    input_format: List[str] | dict | str | None = None,
    creation_option: List[str] | dict | str | None = None,
    extent: List[float] | float | None = None,
    resolution: List[float] | float | None = None,
    size: List[int] | int | None = None,
    output_data_type: str | None = None,
    crs: str | None = None,
    overwrite: bool | None = None,
    input_layer: List[str] | dict | str | None = None,
    sql: str | None = None,
    bbox: List[float] | float | None = None,
    zfield: str | None = None,
    zoffset: float | None = None,
    zmultiply: float | None = None,
    power: float | None = None,
    smoothing: float | None = None,
    radius: float | None = None,
    radius1: float | None = None,
    radius2: float | None = None,
    angle: float | None = None,
    min_points: int | None = None,
    max_points: int | None = None,
    min_points_per_quadrant: int | None = None,
    max_points_per_quadrant: int | None = None,
    nodata: float | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Create a regular grid from scattered points using weighted inverse distance interpolation.

    Consult https://gdal.org/programs/gdal_vector_grid.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input vector datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    extent: Optional[Union[List[float], float]]=None
        Set the target georeferenced extent
    resolution: Optional[Union[List[float], float]]=None
        Set the target resolution
    size: Optional[Union[List[int], int]]=None
        Set the target size in pixels and lines
    output_data_type: Optional[str]=None
        Aliases: datatype
        Output data type
    crs: Optional[str]=None
        Override the projection for the output file
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    input_layer: Optional[Union[List[str], dict, str]]=None
        Aliases: layer
        Input layer name
    sql: Optional[str]=None
        SQL statement
    bbox: Optional[Union[List[float], float]]=None
        Select only points contained within the specified bounding box
    zfield: Optional[str]=None
        Field name from which to get Z values.
    zoffset: Optional[float]=None
        Value to add to the Z field value (applied before zmultiply)
    zmultiply: Optional[float]=None
        Multiplication factor for the Z field value (applied after zoffset)
    power: Optional[float]=None
        Weighting power
    smoothing: Optional[float]=None
        Smoothing parameter
    radius: Optional[float]=None
        Radius of the search circle
    radius1: Optional[float]=None
        First axis of the search ellipse
    radius2: Optional[float]=None
        Second axis of the search ellipse
    angle: Optional[float]=None
        Angle of search ellipse rotation in degrees (counter clockwise)
    min_points: Optional[int]=None
        Minimum number of data points to use
    max_points: Optional[int]=None
        Maximum number of data points to use
    min_points_per_quadrant: Optional[int]=None
        Minimum number of data points to use per quadrant
    max_points_per_quadrant: Optional[int]=None
        Maximum number of data points to use per quadrant
    nodata: Optional[float]=None
        Target nodata value
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def invdistnn(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    quiet: bool | None = None,
    output_format: str | None = None,
    open_option: List[str] | dict | str | None = None,
    input_format: List[str] | dict | str | None = None,
    creation_option: List[str] | dict | str | None = None,
    extent: List[float] | float | None = None,
    resolution: List[float] | float | None = None,
    size: List[int] | int | None = None,
    output_data_type: str | None = None,
    crs: str | None = None,
    overwrite: bool | None = None,
    input_layer: List[str] | dict | str | None = None,
    sql: str | None = None,
    bbox: List[float] | float | None = None,
    zfield: str | None = None,
    zoffset: float | None = None,
    zmultiply: float | None = None,
    power: float | None = None,
    smoothing: float | None = None,
    radius: float | None = None,
    min_points: int | None = None,
    max_points: int | None = None,
    min_points_per_quadrant: int | None = None,
    max_points_per_quadrant: int | None = None,
    nodata: float | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Create a regular grid from scattered points using weighted inverse distance interpolation nearest neighbour.

    Consult https://gdal.org/programs/gdal_vector_grid.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input vector datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    extent: Optional[Union[List[float], float]]=None
        Set the target georeferenced extent
    resolution: Optional[Union[List[float], float]]=None
        Set the target resolution
    size: Optional[Union[List[int], int]]=None
        Set the target size in pixels and lines
    output_data_type: Optional[str]=None
        Aliases: datatype
        Output data type
    crs: Optional[str]=None
        Override the projection for the output file
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    input_layer: Optional[Union[List[str], dict, str]]=None
        Aliases: layer
        Input layer name
    sql: Optional[str]=None
        SQL statement
    bbox: Optional[Union[List[float], float]]=None
        Select only points contained within the specified bounding box
    zfield: Optional[str]=None
        Field name from which to get Z values.
    zoffset: Optional[float]=None
        Value to add to the Z field value (applied before zmultiply)
    zmultiply: Optional[float]=None
        Multiplication factor for the Z field value (applied after zoffset)
    power: Optional[float]=None
        Weighting power
    smoothing: Optional[float]=None
        Smoothing parameter
    radius: Optional[float]=None
        Radius of the search circle
    min_points: Optional[int]=None
        Minimum number of data points to use
    max_points: Optional[int]=None
        Maximum number of data points to use
    min_points_per_quadrant: Optional[int]=None
        Minimum number of data points to use per quadrant
    max_points_per_quadrant: Optional[int]=None
        Maximum number of data points to use per quadrant
    nodata: Optional[float]=None
        Target nodata value
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def linear(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    quiet: bool | None = None,
    output_format: str | None = None,
    open_option: List[str] | dict | str | None = None,
    input_format: List[str] | dict | str | None = None,
    creation_option: List[str] | dict | str | None = None,
    extent: List[float] | float | None = None,
    resolution: List[float] | float | None = None,
    size: List[int] | int | None = None,
    output_data_type: str | None = None,
    crs: str | None = None,
    overwrite: bool | None = None,
    input_layer: List[str] | dict | str | None = None,
    sql: str | None = None,
    bbox: List[float] | float | None = None,
    zfield: str | None = None,
    zoffset: float | None = None,
    zmultiply: float | None = None,
    radius: float | None = None,
    nodata: float | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Create a regular grid from scattered points using linear/barycentric interpolation.

    Consult https://gdal.org/programs/gdal_vector_grid.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input vector datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    extent: Optional[Union[List[float], float]]=None
        Set the target georeferenced extent
    resolution: Optional[Union[List[float], float]]=None
        Set the target resolution
    size: Optional[Union[List[int], int]]=None
        Set the target size in pixels and lines
    output_data_type: Optional[str]=None
        Aliases: datatype
        Output data type
    crs: Optional[str]=None
        Override the projection for the output file
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    input_layer: Optional[Union[List[str], dict, str]]=None
        Aliases: layer
        Input layer name
    sql: Optional[str]=None
        SQL statement
    bbox: Optional[Union[List[float], float]]=None
        Select only points contained within the specified bounding box
    zfield: Optional[str]=None
        Field name from which to get Z values.
    zoffset: Optional[float]=None
        Value to add to the Z field value (applied before zmultiply)
    zmultiply: Optional[float]=None
        Multiplication factor for the Z field value (applied after zoffset)
    radius: Optional[float]=None
        Radius of the search circle
    nodata: Optional[float]=None
        Target nodata value
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def maximum(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    quiet: bool | None = None,
    output_format: str | None = None,
    open_option: List[str] | dict | str | None = None,
    input_format: List[str] | dict | str | None = None,
    creation_option: List[str] | dict | str | None = None,
    extent: List[float] | float | None = None,
    resolution: List[float] | float | None = None,
    size: List[int] | int | None = None,
    output_data_type: str | None = None,
    crs: str | None = None,
    overwrite: bool | None = None,
    input_layer: List[str] | dict | str | None = None,
    sql: str | None = None,
    bbox: List[float] | float | None = None,
    zfield: str | None = None,
    zoffset: float | None = None,
    zmultiply: float | None = None,
    radius: float | None = None,
    radius1: float | None = None,
    radius2: float | None = None,
    angle: float | None = None,
    min_points: int | None = None,
    min_points_per_quadrant: int | None = None,
    max_points_per_quadrant: int | None = None,
    nodata: float | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Create a regular grid from scattered points using the maximum value in the search ellipse.

    Consult https://gdal.org/programs/gdal_vector_grid.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input vector datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    extent: Optional[Union[List[float], float]]=None
        Set the target georeferenced extent
    resolution: Optional[Union[List[float], float]]=None
        Set the target resolution
    size: Optional[Union[List[int], int]]=None
        Set the target size in pixels and lines
    output_data_type: Optional[str]=None
        Aliases: datatype
        Output data type
    crs: Optional[str]=None
        Override the projection for the output file
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    input_layer: Optional[Union[List[str], dict, str]]=None
        Aliases: layer
        Input layer name
    sql: Optional[str]=None
        SQL statement
    bbox: Optional[Union[List[float], float]]=None
        Select only points contained within the specified bounding box
    zfield: Optional[str]=None
        Field name from which to get Z values.
    zoffset: Optional[float]=None
        Value to add to the Z field value (applied before zmultiply)
    zmultiply: Optional[float]=None
        Multiplication factor for the Z field value (applied after zoffset)
    radius: Optional[float]=None
        Radius of the search circle
    radius1: Optional[float]=None
        First axis of the search ellipse
    radius2: Optional[float]=None
        Second axis of the search ellipse
    angle: Optional[float]=None
        Angle of search ellipse rotation in degrees (counter clockwise)
    min_points: Optional[int]=None
        Minimum number of data points to use
    min_points_per_quadrant: Optional[int]=None
        Minimum number of data points to use per quadrant
    max_points_per_quadrant: Optional[int]=None
        Maximum number of data points to use per quadrant
    nodata: Optional[float]=None
        Target nodata value
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def minimum(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    quiet: bool | None = None,
    output_format: str | None = None,
    open_option: List[str] | dict | str | None = None,
    input_format: List[str] | dict | str | None = None,
    creation_option: List[str] | dict | str | None = None,
    extent: List[float] | float | None = None,
    resolution: List[float] | float | None = None,
    size: List[int] | int | None = None,
    output_data_type: str | None = None,
    crs: str | None = None,
    overwrite: bool | None = None,
    input_layer: List[str] | dict | str | None = None,
    sql: str | None = None,
    bbox: List[float] | float | None = None,
    zfield: str | None = None,
    zoffset: float | None = None,
    zmultiply: float | None = None,
    radius: float | None = None,
    radius1: float | None = None,
    radius2: float | None = None,
    angle: float | None = None,
    min_points: int | None = None,
    min_points_per_quadrant: int | None = None,
    max_points_per_quadrant: int | None = None,
    nodata: float | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Create a regular grid from scattered points using the minimum value in the search ellipse.

    Consult https://gdal.org/programs/gdal_vector_grid.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input vector datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    extent: Optional[Union[List[float], float]]=None
        Set the target georeferenced extent
    resolution: Optional[Union[List[float], float]]=None
        Set the target resolution
    size: Optional[Union[List[int], int]]=None
        Set the target size in pixels and lines
    output_data_type: Optional[str]=None
        Aliases: datatype
        Output data type
    crs: Optional[str]=None
        Override the projection for the output file
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    input_layer: Optional[Union[List[str], dict, str]]=None
        Aliases: layer
        Input layer name
    sql: Optional[str]=None
        SQL statement
    bbox: Optional[Union[List[float], float]]=None
        Select only points contained within the specified bounding box
    zfield: Optional[str]=None
        Field name from which to get Z values.
    zoffset: Optional[float]=None
        Value to add to the Z field value (applied before zmultiply)
    zmultiply: Optional[float]=None
        Multiplication factor for the Z field value (applied after zoffset)
    radius: Optional[float]=None
        Radius of the search circle
    radius1: Optional[float]=None
        First axis of the search ellipse
    radius2: Optional[float]=None
        Second axis of the search ellipse
    angle: Optional[float]=None
        Angle of search ellipse rotation in degrees (counter clockwise)
    min_points: Optional[int]=None
        Minimum number of data points to use
    min_points_per_quadrant: Optional[int]=None
        Minimum number of data points to use per quadrant
    max_points_per_quadrant: Optional[int]=None
        Maximum number of data points to use per quadrant
    nodata: Optional[float]=None
        Target nodata value
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def nearest(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    quiet: bool | None = None,
    output_format: str | None = None,
    open_option: List[str] | dict | str | None = None,
    input_format: List[str] | dict | str | None = None,
    creation_option: List[str] | dict | str | None = None,
    extent: List[float] | float | None = None,
    resolution: List[float] | float | None = None,
    size: List[int] | int | None = None,
    output_data_type: str | None = None,
    crs: str | None = None,
    overwrite: bool | None = None,
    input_layer: List[str] | dict | str | None = None,
    sql: str | None = None,
    bbox: List[float] | float | None = None,
    zfield: str | None = None,
    zoffset: float | None = None,
    zmultiply: float | None = None,
    radius: float | None = None,
    radius1: float | None = None,
    radius2: float | None = None,
    angle: float | None = None,
    nodata: float | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Create a regular grid from scattered points using nearest neighbor interpolation.

    Consult https://gdal.org/programs/gdal_vector_grid.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input vector datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    extent: Optional[Union[List[float], float]]=None
        Set the target georeferenced extent
    resolution: Optional[Union[List[float], float]]=None
        Set the target resolution
    size: Optional[Union[List[int], int]]=None
        Set the target size in pixels and lines
    output_data_type: Optional[str]=None
        Aliases: datatype
        Output data type
    crs: Optional[str]=None
        Override the projection for the output file
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    input_layer: Optional[Union[List[str], dict, str]]=None
        Aliases: layer
        Input layer name
    sql: Optional[str]=None
        SQL statement
    bbox: Optional[Union[List[float], float]]=None
        Select only points contained within the specified bounding box
    zfield: Optional[str]=None
        Field name from which to get Z values.
    zoffset: Optional[float]=None
        Value to add to the Z field value (applied before zmultiply)
    zmultiply: Optional[float]=None
        Multiplication factor for the Z field value (applied after zoffset)
    radius: Optional[float]=None
        Radius of the search circle
    radius1: Optional[float]=None
        First axis of the search ellipse
    radius2: Optional[float]=None
        Second axis of the search ellipse
    angle: Optional[float]=None
        Angle of search ellipse rotation in degrees (counter clockwise)
    nodata: Optional[float]=None
        Target nodata value
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def range(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    quiet: bool | None = None,
    output_format: str | None = None,
    open_option: List[str] | dict | str | None = None,
    input_format: List[str] | dict | str | None = None,
    creation_option: List[str] | dict | str | None = None,
    extent: List[float] | float | None = None,
    resolution: List[float] | float | None = None,
    size: List[int] | int | None = None,
    output_data_type: str | None = None,
    crs: str | None = None,
    overwrite: bool | None = None,
    input_layer: List[str] | dict | str | None = None,
    sql: str | None = None,
    bbox: List[float] | float | None = None,
    zfield: str | None = None,
    zoffset: float | None = None,
    zmultiply: float | None = None,
    radius: float | None = None,
    radius1: float | None = None,
    radius2: float | None = None,
    angle: float | None = None,
    min_points: int | None = None,
    min_points_per_quadrant: int | None = None,
    max_points_per_quadrant: int | None = None,
    nodata: float | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Create a regular grid from scattered points using the difference between the minimum and maximum values in the search ellipse.

    Consult https://gdal.org/programs/gdal_vector_grid.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input vector datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    extent: Optional[Union[List[float], float]]=None
        Set the target georeferenced extent
    resolution: Optional[Union[List[float], float]]=None
        Set the target resolution
    size: Optional[Union[List[int], int]]=None
        Set the target size in pixels and lines
    output_data_type: Optional[str]=None
        Aliases: datatype
        Output data type
    crs: Optional[str]=None
        Override the projection for the output file
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    input_layer: Optional[Union[List[str], dict, str]]=None
        Aliases: layer
        Input layer name
    sql: Optional[str]=None
        SQL statement
    bbox: Optional[Union[List[float], float]]=None
        Select only points contained within the specified bounding box
    zfield: Optional[str]=None
        Field name from which to get Z values.
    zoffset: Optional[float]=None
        Value to add to the Z field value (applied before zmultiply)
    zmultiply: Optional[float]=None
        Multiplication factor for the Z field value (applied after zoffset)
    radius: Optional[float]=None
        Radius of the search circle
    radius1: Optional[float]=None
        First axis of the search ellipse
    radius2: Optional[float]=None
        Second axis of the search ellipse
    angle: Optional[float]=None
        Angle of search ellipse rotation in degrees (counter clockwise)
    min_points: Optional[int]=None
        Minimum number of data points to use
    min_points_per_quadrant: Optional[int]=None
        Minimum number of data points to use per quadrant
    max_points_per_quadrant: Optional[int]=None
        Maximum number of data points to use per quadrant
    nodata: Optional[float]=None
        Target nodata value
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...
