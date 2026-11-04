import os
from collections.abc import Callable
from typing import List

import osgeo.gdal
from osgeo import gdal

def as_features(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    input_format: List[str] | dict | str | None = None,
    open_option: List[str] | dict | str | None = None,
    output_format: str | None = None,
    output_open_option: List[str] | dict | str | None = None,
    creation_option: List[str] | dict | str | None = None,
    layer_creation_option: List[str] | dict | str | None = None,
    overwrite: bool | None = None,
    update: bool | None = None,
    overwrite_layer: bool | None = None,
    append: bool | None = None,
    output_layer: str | None = None,
    band: List[int] | int | None = None,
    geometry_type: str | None = None,
    skip_nodata: bool | None = None,
    include_xy: bool | None = None,
    include_row_col: bool | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Create features from pixels of a raster dataset

    Consult https://gdal.org/programs/gdal_raster_as_features.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input raster datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output vector dataset
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    output_format: Optional[str]=None
        Aliases: format
        Output format ("GDALG" allowed)
    output_open_option: Optional[Union[List[str], dict, str]]=None
        Aliases: output_oo
        Output open options
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    layer_creation_option: Optional[Union[List[str], dict, str]]=None
        Layer creation option
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    update: Optional[bool]=None
        Whether to open existing dataset in update mode
    overwrite_layer: Optional[bool]=None
        Whether overwriting existing output layer is allowed
    append: Optional[bool]=None
        Whether appending to existing layer is allowed
    output_layer: Optional[str]=None
        Output layer name
    band: Optional[Union[List[int], int]]=None
        Input band(s) (1-based index)
    geometry_type: Optional[str]=None
        Geometry type
    skip_nodata: Optional[bool]=None
        Omit NoData pixels from the result
    include_xy: Optional[bool]=None
        Include fields for cell center coordinates
    include_row_col: Optional[bool]=None
        Include columns for row and column
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output vector dataset


    """
    ...

def aspect(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    input_format: List[str] | dict | str | None = None,
    open_option: List[str] | dict | str | None = None,
    quiet: bool | None = None,
    output_format: str | None = None,
    creation_option: List[str] | dict | str | None = None,
    overwrite: bool | None = None,
    append: bool | None = None,
    band: int | None = None,
    convention: str | None = None,
    gradient_alg: str | None = None,
    zero_for_flat: bool | None = None,
    no_edges: bool | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Generate an aspect map

    Consult https://gdal.org/programs/gdal_raster_aspect.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input raster datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format ("GDALG" allowed)
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    append: Optional[bool]=None
        Append as a subdataset to existing output
    band: Optional[int]=None
        Input band (1-based index)
    convention: Optional[str]=None
        Convention for output angles
    gradient_alg: Optional[str]=None
        Algorithm used to compute terrain gradient
    zero_for_flat: Optional[bool]=None
        Whether to output zero for flat areas
    no_edges: Optional[bool]=None
        Do not try to interpolate values at dataset edges or close to nodata values
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def blend(
    overlay: osgeo.gdal.Dataset | str | os.PathLike[str],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    input_format: List[str] | dict | str | None = None,
    open_option: List[str] | dict | str | None = None,
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]] | None = None,
    quiet: bool | None = None,
    output_format: str | None = None,
    creation_option: List[str] | dict | str | None = None,
    overwrite: bool | None = None,
    append: bool | None = None,
    operator: str | None = None,
    opacity: int | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Blend/compose two raster datasets

    Consult https://gdal.org/programs/gdal_raster_blend.html for more details.

    Parameters
    ----------
    overlay: Union[gdal.Dataset, str, os.PathLike[str]]
        Overlay dataset
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Aliases: color_input
        Input raster dataset
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format ("GDALG" allowed)
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    append: Optional[bool]=None
        Append as a subdataset to existing output
    operator: Optional[str]=None
        Composition operator
    opacity: Optional[int]=None
        Opacity percentage to apply to the overlay dataset (0=fully transparent, 100=full use of overlay opacity)
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def calc(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    calc: List[str] | dict | str,
    input_format: List[str] | dict | str | None = None,
    open_option: List[str] | dict | str | None = None,
    quiet: bool | None = None,
    output_format: str | None = None,
    creation_option: List[str] | dict | str | None = None,
    overwrite: bool | None = None,
    append: bool | None = None,
    output_data_type: str | None = None,
    no_check_crs: bool | None = None,
    no_check_extent: bool | None = None,
    propagate_nodata: bool | None = None,
    dialect: str | None = None,
    flatten: bool | None = None,
    nodata: str | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Perform raster algebra

    Consult https://gdal.org/programs/gdal_raster_calc.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input raster datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    calc: Union[List[str], dict, str]
        Expression(s) to evaluate
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format ("GDALG" allowed)
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    append: Optional[bool]=None
        Append as a subdataset to existing output
    output_data_type: Optional[str]=None
        Aliases: datatype
        Output data type
    no_check_crs: Optional[bool]=None
        Do not check consistency of input coordinate reference systems
    no_check_extent: Optional[bool]=None
        Do not check consistency of input extents
    propagate_nodata: Optional[bool]=None
        Whether to set pixels to the output NoData value if any of the input pixels is NoData
    dialect: Optional[str]=None
        Expression dialect
    flatten: Optional[bool]=None
        Generate a single band output raster per expression, even if input datasets are multiband
    nodata: Optional[str]=None
        Assign a specified nodata value to output bands ('none', numeric value, 'nan', 'inf', '-inf')
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def clean_collar(
    input: osgeo.gdal.Dataset | str | os.PathLike[str],
    quiet: bool | None = None,
    open_option: List[str] | dict | str | None = None,
    input_format: List[str] | dict | str | None = None,
    output: osgeo.gdal.Dataset | str | os.PathLike[str] | None = None,
    output_format: str | None = None,
    creation_option: List[str] | dict | str | None = None,
    overwrite: bool | None = None,
    update: bool | None = None,
    color: List[str] | dict | str | None = None,
    color_threshold: int | None = None,
    pixel_distance: int | None = None,
    add_alpha: bool | None = None,
    add_mask: bool | None = None,
    algorithm: str | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Clean the collar of a raster dataset, removing noise.

    Consult https://gdal.org/programs/gdal_raster_clean_collar.html for more details.

    Parameters
    ----------
    input: Union[gdal.Dataset, str, os.PathLike[str]]
        Input raster dataset
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    output: Optional[Union[gdal.Dataset, str, os.PathLike[str]]]=None
        Output raster dataset
    output_format: Optional[str]=None
        Aliases: format
        Output format
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    update: Optional[bool]=None
        Whether to open existing dataset in update mode
    color: Optional[Union[List[str], dict, str]]=None
        Transparent color(s): tuple of integer (like 'r,g,b'), 'black', 'white'
    color_threshold: Optional[int]=None
        Select how far from specified transparent colors the pixel values are considered transparent.
    pixel_distance: Optional[int]=None
        Number of consecutive transparent pixels that can be encountered before the giving up search inwards.
    add_alpha: Optional[bool]=None
        Adds an alpha band to the output dataset.
    add_mask: Optional[bool]=None
        Adds a mask band to the output dataset.
    algorithm: Optional[str]=None
        Algorithm to apply
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def clip(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    input_format: List[str] | dict | str | None = None,
    open_option: List[str] | dict | str | None = None,
    quiet: bool | None = None,
    output_format: str | None = None,
    creation_option: List[str] | dict | str | None = None,
    overwrite: bool | None = None,
    append: bool | None = None,
    bbox: List[float] | float | None = None,
    bbox_crs: str | None = None,
    window: List[int] | int | None = None,
    geometry: str | None = None,
    geometry_crs: str | None = None,
    like: osgeo.gdal.Dataset | str | os.PathLike[str] | None = None,
    like_sql: str | None = None,
    like_layer: str | None = None,
    like_where: str | None = None,
    only_bbox: bool | None = None,
    allow_bbox_outside_source: bool | None = None,
    add_alpha: bool | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Clip a raster dataset.

    Consult https://gdal.org/programs/gdal_raster_clip.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input raster datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format ("GDALG" allowed)
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    append: Optional[bool]=None
        Append as a subdataset to existing output
    bbox: Optional[Union[List[float], float]]=None
        Clipping bounding box as xmin,ymin,xmax,ymax
    bbox_crs: Optional[str]=None
        CRS of clipping bounding box
    window: Optional[Union[List[int], int]]=None
        Raster window as col,line,width,height in pixels
    geometry: Optional[str]=None
        Clipping geometry (WKT or GeoJSON)
    geometry_crs: Optional[str]=None
        CRS of clipping geometry
    like: Optional[Union[gdal.Dataset, str, os.PathLike[str]]]=None
        Dataset to use as a template for bounds
    like_sql: Optional[str]=None
        SELECT statement to run on the 'like' dataset
    like_layer: Optional[str]=None
        Name of the layer of the 'like' dataset
    like_where: Optional[str]=None
        WHERE SQL clause to run on the 'like' dataset
    only_bbox: Optional[bool]=None
        For 'geometry' and 'like', only consider their bounding box
    allow_bbox_outside_source: Optional[bool]=None
        Allow clipping box to include pixels outside input dataset
    add_alpha: Optional[bool]=None
        Adds an alpha mask band to the destination when the source raster have none.
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def color_map(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    input_format: List[str] | dict | str | None = None,
    open_option: List[str] | dict | str | None = None,
    quiet: bool | None = None,
    output_format: str | None = None,
    creation_option: List[str] | dict | str | None = None,
    overwrite: bool | None = None,
    append: bool | None = None,
    band: int | None = None,
    color_map: str | None = None,
    add_alpha: bool | None = None,
    color_selection: str | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Generate a RGB or RGBA dataset from a single band, using a color map

    Consult https://gdal.org/programs/gdal_raster_color_map.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input raster datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format ("GDALG" allowed)
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    append: Optional[bool]=None
        Append as a subdataset to existing output
    band: Optional[int]=None
        Input band (1-based index)
    color_map: Optional[str]=None
        Color map filename
    add_alpha: Optional[bool]=None
        Adds an alpha mask band to the destination.
    color_selection: Optional[str]=None
        How to compute output colors from input values
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def compare(
    reference: osgeo.gdal.Dataset | str | os.PathLike[str],
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    quiet: bool | None = None,
    input_format: List[str] | dict | str | None = None,
    open_option: List[str] | dict | str | None = None,
    skip_all_optional: bool | None = None,
    skip_binary: bool | None = None,
    skip_crs: bool | None = None,
    skip_geotransform: bool | None = None,
    skip_overview: bool | None = None,
    skip_metadata: bool | None = None,
    skip_rpc: bool | None = None,
    skip_geolocation: bool | None = None,
    skip_subdataset: bool | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Compare two raster datasets.

    Consult https://gdal.org/programs/gdal_raster_compare.html for more details.

    Parameters
    ----------
    reference: Union[gdal.Dataset, str, os.PathLike[str]]
        Reference dataset
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input raster dataset
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    skip_all_optional: Optional[bool]=None
        Skip all optional comparisons
    skip_binary: Optional[bool]=None
        Skip binary file comparison
    skip_crs: Optional[bool]=None
        Skip CRS comparison
    skip_geotransform: Optional[bool]=None
        Skip geotransform comparison
    skip_overview: Optional[bool]=None
        Skip overview comparison
    skip_metadata: Optional[bool]=None
        Skip metadata comparison
    skip_rpc: Optional[bool]=None
        Skip RPC metadata comparison
    skip_geolocation: Optional[bool]=None
        Skip Geolocation metadata comparison
    skip_subdataset: Optional[bool]=None
        Skip subdataset comparison
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output_string: str
        Output string, in which the result is placed
    return_code: int
        Return code


    """
    ...

def contour(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    quiet: bool | None = None,
    input_format: List[str] | dict | str | None = None,
    open_option: List[str] | dict | str | None = None,
    output_format: str | None = None,
    output_open_option: List[str] | dict | str | None = None,
    creation_option: List[str] | dict | str | None = None,
    layer_creation_option: List[str] | dict | str | None = None,
    overwrite: bool | None = None,
    output_layer: str | None = None,
    band: int | None = None,
    elevation_name: str | None = None,
    min_name: str | None = None,
    max_name: str | None = None,
    _3d: bool | None = None,
    input_nodata: float | None = None,
    interval: float | None = None,
    levels: List[str] | dict | str | None = None,
    exp_base: int | None = None,
    offset: float | None = None,
    polygonize: bool | None = None,
    group_transactions: int | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Creates a vector contour from a raster elevation model (DEM).

    Consult https://gdal.org/programs/gdal_raster_contour.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input raster datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output vector dataset
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    output_format: Optional[str]=None
        Aliases: format
        Output format ("GDALG" allowed)
    output_open_option: Optional[Union[List[str], dict, str]]=None
        Aliases: output_oo
        Output open options
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    layer_creation_option: Optional[Union[List[str], dict, str]]=None
        Layer creation option
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    output_layer: Optional[str]=None
        Output layer name
    band: Optional[int]=None
        Input band (1-based index)
    elevation_name: Optional[str]=None
        Name of the elevation field
    min_name: Optional[str]=None
        Name of the minimum elevation field
    max_name: Optional[str]=None
        Name of the maximum elevation field
    _3d: Optional[bool]=None
        Force production of 3D vectors instead of 2D
    input_nodata: Optional[float]=None
        Input pixel value to treat as 'nodata'
    interval: Optional[float]=None
        Elevation interval between contours
    levels: Optional[Union[List[str], dict, str]]=None
        List of contour levels
    exp_base: Optional[int]=None
        Base for exponential contour level generation
    offset: Optional[float]=None
        Offset to apply to contour levels
    polygonize: Optional[bool]=None
        Create polygons instead of lines
    group_transactions: Optional[int]=None
        Group n features per transaction (default 100 000)
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output vector dataset


    """
    ...

def convert(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    input_format: List[str] | dict | str | None = None,
    open_option: List[str] | dict | str | None = None,
    quiet: bool | None = None,
    output_format: str | None = None,
    creation_option: List[str] | dict | str | None = None,
    overwrite: bool | None = None,
    append: bool | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Convert a raster dataset.

    Consult https://gdal.org/programs/gdal_raster_convert.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input raster datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format ("GDALG" allowed)
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    append: Optional[bool]=None
        Append as a subdataset to existing output
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def create(
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    input_format: List[str] | dict | str | None = None,
    open_option: List[str] | dict | str | None = None,
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]] | None = None,
    quiet: bool | None = None,
    output_format: str | None = None,
    creation_option: List[str] | dict | str | None = None,
    overwrite: bool | None = None,
    append: bool | None = None,
    size: List[int] | int | None = None,
    band_count: int | None = None,
    output_data_type: str | None = None,
    nodata: str | None = None,
    burn: List[float] | float | None = None,
    crs: str | None = None,
    bbox: List[float] | float | None = None,
    metadata: List[str] | dict | str | None = None,
    copy_metadata: bool | None = None,
    copy_overviews: bool | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Create a new raster dataset.

    Consult https://gdal.org/programs/gdal_raster_create.html for more details.

    Parameters
    ----------
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    input: Optional[Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]]=None
        Aliases: like
        Template raster dataset
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format ("GDALG" allowed)
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    append: Optional[bool]=None
        Append as a subdataset to existing output
    size: Optional[Union[List[int], int]]=None
        Output size in pixels
    band_count: Optional[int]=None
        Number of bands
    output_data_type: Optional[str]=None
        Aliases: datatype
        Output data type
    nodata: Optional[str]=None
        Assign a specified nodata value to output bands ('none', numeric value, 'nan', 'inf', '-inf')
    burn: Optional[Union[List[float], float]]=None
        Burn value
    crs: Optional[str]=None
        Set CRS
    bbox: Optional[Union[List[float], float]]=None
        Bounding box as xmin,ymin,xmax,ymax
    metadata: Optional[Union[List[str], dict, str]]=None
        Add metadata item
    copy_metadata: Optional[bool]=None
        Copy metadata from input dataset
    copy_overviews: Optional[bool]=None
        Create same overview levels as input dataset
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def edit(
    dataset: osgeo.gdal.Dataset | str | os.PathLike[str],
    quiet: bool | None = None,
    open_option: List[str] | dict | str | None = None,
    auxiliary: bool | None = None,
    band: int | None = None,
    crs: str | None = None,
    bbox: List[float] | float | None = None,
    nodata: str | None = None,
    color_interpretation: List[str] | dict | str | None = None,
    color_map: str | None = None,
    scale: List[str] | dict | str | None = None,
    offset: List[str] | dict | str | None = None,
    metadata: List[str] | dict | str | None = None,
    unset_color_table: bool | None = None,
    unset_metadata: List[str] | dict | str | None = None,
    unset_metadata_domain: List[str] | dict | str | None = None,
    gcp: List[str] | dict | str | None = None,
    stats: bool | None = None,
    approx_stats: bool | None = None,
    hist: bool | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Edit a raster dataset.

    Consult https://gdal.org/programs/gdal_raster_edit.html for more details.

    Parameters
    ----------
    dataset: Union[gdal.Dataset, str, os.PathLike[str]]
        Dataset (to be updated in-place, unless --auxiliary)
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    auxiliary: Optional[bool]=None
        Ask for an auxiliary .aux.xml file to be edited
    band: Optional[int]=None
        Active band (1-based index)
    crs: Optional[str]=None
        Override CRS (without reprojection)
    bbox: Optional[Union[List[float], float]]=None
        Bounding box as xmin,ymin,xmax,ymax
    nodata: Optional[str]=None
        Assign a specified nodata value to output bands ('none', numeric value, 'nan', 'inf', '-inf')
    color_interpretation: Optional[Union[List[str], dict, str]]=None
        Set band color interpretation
    color_map: Optional[str]=None
        Color map filename
    scale: Optional[Union[List[str], dict, str]]=None
        Override band scale factor
    offset: Optional[Union[List[str], dict, str]]=None
        Override band offset constant
    metadata: Optional[Union[List[str], dict, str]]=None
        Add/update dataset metadata item
    unset_color_table: Optional[bool]=None
        Unset color table on 1st band or the one specified with --band
    unset_metadata: Optional[Union[List[str], dict, str]]=None
        Remove dataset metadata item(s)
    unset_metadata_domain: Optional[Union[List[str], dict, str]]=None
        Remove dataset metadata domain(s)
    gcp: Optional[Union[List[str], dict, str]]=None
        Add ground control point, formatted as pixel,line,easting,northing[,elevation], or @filename
    stats: Optional[bool]=None
        Compute statistics, using all pixels
    approx_stats: Optional[bool]=None
        Compute statistics, using a subset of pixels
    hist: Optional[bool]=None
        Compute histogram
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------


    """
    ...

def fill_nodata(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    input_format: List[str] | dict | str | None = None,
    open_option: List[str] | dict | str | None = None,
    quiet: bool | None = None,
    output_format: str | None = None,
    creation_option: List[str] | dict | str | None = None,
    overwrite: bool | None = None,
    append: bool | None = None,
    band: int | None = None,
    max_distance: int | None = None,
    smoothing_iterations: int | None = None,
    mask: osgeo.gdal.Dataset | str | os.PathLike[str] | None = None,
    strategy: str | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Fill nodata raster regions by interpolation from edges.

    Consult https://gdal.org/programs/gdal_raster_fill_nodata.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input raster datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format ("GDALG" allowed)
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    append: Optional[bool]=None
        Append as a subdataset to existing output
    band: Optional[int]=None
        Input band (1-based index)
    max_distance: Optional[int]=None
        The maximum distance (in pixels) that the algorithm will search out for values to interpolate.
    smoothing_iterations: Optional[int]=None
        The number of 3x3 average filter smoothing iterations to run after the interpolation to dampen artifacts. The default is zero smoothing iterations.
    mask: Optional[Union[gdal.Dataset, str, os.PathLike[str]]]=None
        Use the first band of the specified file as a validity mask (zero is invalid, non-zero is valid).
    strategy: Optional[str]=None
        By default, pixels are interpolated using an inverse distance weighting (invdist). It is also possible to choose a nearest neighbour (nearest) strategy.
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def footprint(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    quiet: bool | None = None,
    open_option: List[str] | dict | str | None = None,
    input_format: List[str] | dict | str | None = None,
    output_format: str | None = None,
    creation_option: List[str] | dict | str | None = None,
    layer_creation_option: List[str] | dict | str | None = None,
    append: bool | None = None,
    overwrite: bool | None = None,
    output_layer: str | None = None,
    band: List[int] | int | None = None,
    combine_bands: str | None = None,
    overview: int | None = None,
    input_nodata: List[float] | float | None = None,
    coordinate_system: str | None = None,
    output_crs: str | None = None,
    split_multipolygons: bool | None = None,
    convex_hull: bool | None = None,
    densify_distance: float | None = None,
    simplify_tolerance: float | None = None,
    min_ring_area: float | None = None,
    max_points: str | None = None,
    location_field: str | None = None,
    no_location_field: bool | None = None,
    absolute_path: bool | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Compute the footprint of a raster dataset.

    Consult https://gdal.org/programs/gdal_raster_footprint.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input raster datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output vector dataset
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    output_format: Optional[str]=None
        Aliases: format
        Output format
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    layer_creation_option: Optional[Union[List[str], dict, str]]=None
        Layer creation option
    append: Optional[bool]=None
        Whether appending to existing layer is allowed
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    output_layer: Optional[str]=None
        Output layer name
    band: Optional[Union[List[int], int]]=None
        Input band(s) (1-based index)
    combine_bands: Optional[str]=None
        Defines how the mask bands of the selected bands are combined to generate a single mask band, before being vectorized.
    overview: Optional[int]=None
        Which overview level of source file must be used
    input_nodata: Optional[Union[List[float], float]]=None
        Set nodata values for input bands.
    coordinate_system: Optional[str]=None
        Target coordinate system
    output_crs: Optional[str]=None
        Output CRS
    split_multipolygons: Optional[bool]=None
        Whether to split multipolygons as several features each with one single polygon
    convex_hull: Optional[bool]=None
        Whether to compute the convex hull of the footprint
    densify_distance: Optional[float]=None
        Maximum distance between 2 consecutive points of the output geometry.
    simplify_tolerance: Optional[float]=None
        Tolerance used to merge consecutive points of the output geometry.
    min_ring_area: Optional[float]=None
        Minimum value for the area of a ring
    max_points: Optional[str]=None
        Maximum number of points of each output geometry
    location_field: Optional[str]=None
        Name of the field where the path of the input dataset will be stored.
    no_location_field: Optional[bool]=None
        Disable creating a field with the path of the input dataset
    absolute_path: Optional[bool]=None
        Whether the path to the input dataset should be stored as an absolute path
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output vector dataset


    """
    ...

def hillshade(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    input_format: List[str] | dict | str | None = None,
    open_option: List[str] | dict | str | None = None,
    quiet: bool | None = None,
    output_format: str | None = None,
    creation_option: List[str] | dict | str | None = None,
    overwrite: bool | None = None,
    append: bool | None = None,
    band: int | None = None,
    zfactor: float | None = None,
    xscale: float | None = None,
    yscale: float | None = None,
    azimuth: float | None = None,
    altitude: float | None = None,
    gradient_alg: str | None = None,
    variant: str | None = None,
    no_edges: bool | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Generate a shaded relief map

    Consult https://gdal.org/programs/gdal_raster_hillshade.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input raster datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format ("GDALG" allowed)
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    append: Optional[bool]=None
        Append as a subdataset to existing output
    band: Optional[int]=None
        Input band (1-based index)
    zfactor: Optional[float]=None
        Vertical exaggeration used to pre-multiply the elevations
    xscale: Optional[float]=None
        Ratio of vertical units to horizontal X axis units
    yscale: Optional[float]=None
        Ratio of vertical units to horizontal Y axis units
    azimuth: Optional[float]=None
        Azimuth of the light, in degrees
    altitude: Optional[float]=None
        Altitude of the light, in degrees
    gradient_alg: Optional[str]=None
        Algorithm used to compute terrain gradient
    variant: Optional[str]=None
        Variant of the hillshading algorithm
    no_edges: Optional[bool]=None
        Do not try to interpolate values at dataset edges or close to nodata values
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def index(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    quiet: bool | None = None,
    output_format: str | None = None,
    creation_option: List[str] | dict | str | None = None,
    layer_creation_option: List[str] | dict | str | None = None,
    overwrite: bool | None = None,
    update: bool | None = None,
    overwrite_layer: bool | None = None,
    append: bool | None = None,
    output_layer: str | None = None,
    recursive: bool | None = None,
    filename_filter: List[str] | dict | str | None = None,
    min_pixel_size: float | None = None,
    max_pixel_size: float | None = None,
    location_name: str | None = None,
    absolute_path: bool | None = None,
    output_crs: str | None = None,
    metadata: List[str] | dict | str | None = None,
    skip_errors: bool | None = None,
    profile: str | None = None,
    base_url: str | None = None,
    id_method: str | None = None,
    id_metadata_item: str | None = None,
    source_crs_field_name: str | None = None,
    source_crs_format: str | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Create a vector index of raster datasets.

    Consult https://gdal.org/programs/gdal_raster_index.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input raster datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output vector dataset
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    layer_creation_option: Optional[Union[List[str], dict, str]]=None
        Layer creation option
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    update: Optional[bool]=None
        Whether to open existing dataset in update mode
    overwrite_layer: Optional[bool]=None
        Whether overwriting existing output layer is allowed
    append: Optional[bool]=None
        Whether appending to existing layer is allowed
    output_layer: Optional[str]=None
        Output layer name
    recursive: Optional[bool]=None
        Whether input directories should be explored recursively.
    filename_filter: Optional[Union[List[str], dict, str]]=None
        Pattern that the filenames in input directories should follow ('*' and '?' wildcard)
    min_pixel_size: Optional[float]=None
        Minimum pixel size in term of geospatial extent per pixel (resolution) that a raster should have to be selected.
    max_pixel_size: Optional[float]=None
        Maximum pixel size in term of geospatial extent per pixel (resolution) that a raster should have to be selected.
    location_name: Optional[str]=None
        Name of the field with the raster path
    absolute_path: Optional[bool]=None
        Whether the path to the input datasets should be stored as an absolute path
    output_crs: Optional[str]=None
        Output CRS
    metadata: Optional[Union[List[str], dict, str]]=None
        Add dataset metadata item
    skip_errors: Optional[bool]=None
        Skip errors related to input datasets
    profile: Optional[str]=None
        Profile of output dataset
    base_url: Optional[str]=None
        Base URL for STAC-GeoParquet href
    id_method: Optional[str]=None
        How to derive STAC-GeoParquet 'id'
    id_metadata_item: Optional[str]=None
        Name of metadata item used to set STAC-GeoParquet 'id'
    source_crs_field_name: Optional[str]=None
        Name of the field to store the CRS of each dataset
    source_crs_format: Optional[str]=None
        Format in which the CRS of each dataset must be written
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output vector dataset


    """
    ...

def info(
    input_format: List[str] | dict | str | None = None,
    open_option: List[str] | dict | str | None = None,
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]] | None = None,
    output_format: str | None = None,
    min_max: bool | None = None,
    stats: bool | None = None,
    approx_stats: bool | None = None,
    hist: bool | None = None,
    no_gcp: bool | None = None,
    no_md: bool | None = None,
    no_ct: bool | None = None,
    no_fl: bool | None = None,
    checksum: bool | None = None,
    list_mdd: bool | None = None,
    metadata_domain: str | None = None,
    no_nodata: bool | None = None,
    no_mask: bool | None = None,
    subdataset: int | None = None,
    crs_format: str | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Return information on a raster dataset.

    Consult https://gdal.org/programs/gdal_raster_info.html for more details.

    Parameters
    ----------
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Aliases: dataset
        Input raster dataset
    output_format: Optional[str]=None
        Aliases: format
        Output format
    min_max: Optional[bool]=None
        Compute minimum and maximum value
    stats: Optional[bool]=None
        Retrieve or compute statistics, using all pixels
    approx_stats: Optional[bool]=None
        Retrieve or compute statistics, using a subset of pixels
    hist: Optional[bool]=None
        Retrieve or compute histogram
    no_gcp: Optional[bool]=None
        Suppress ground control points list printing
    no_md: Optional[bool]=None
        Suppress metadata printing
    no_ct: Optional[bool]=None
        Suppress color table printing
    no_fl: Optional[bool]=None
        Suppress file list printing
    checksum: Optional[bool]=None
        Compute pixel checksum
    list_mdd: Optional[bool]=None
        Aliases: list_metadata_domains
        List all metadata domains available for the dataset
    metadata_domain: Optional[str]=None
        Report metadata for the specified domain. 'all' can be used to report metadata in all domains
    no_nodata: Optional[bool]=None
        Suppress retrieving nodata value
    no_mask: Optional[bool]=None
        Suppress mask band information
    subdataset: Optional[int]=None
        Use subdataset of specified index (starting at 1), instead of the source dataset itself
    crs_format: Optional[str]=None
        Which format to use to report CRS
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output_string: str
        Output string, in which the result is placed


    """
    ...

def mosaic(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    input_format: List[str] | dict | str | None = None,
    open_option: List[str] | dict | str | None = None,
    quiet: bool | None = None,
    output_format: str | None = None,
    creation_option: List[str] | dict | str | None = None,
    overwrite: bool | None = None,
    append: bool | None = None,
    band: List[int] | int | None = None,
    absolute_path: bool | None = None,
    resolution: str | None = None,
    bbox: List[float] | float | None = None,
    target_aligned_pixels: bool | None = None,
    input_nodata: List[float] | float | None = None,
    output_nodata: List[float] | float | None = None,
    hide_nodata: bool | None = None,
    add_alpha: bool | None = None,
    pixel_function: str | None = None,
    pixel_function_arg: List[str] | dict | str | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Build a mosaic, either virtual (VRT) or materialized.

    Consult https://gdal.org/programs/gdal_raster_mosaic.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input raster datasets (or specify a @<filename> to point to a file containing filenames)
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format ("GDALG" allowed)
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    append: Optional[bool]=None
        Append as a subdataset to existing output
    band: Optional[Union[List[int], int]]=None
        Input band(s) (1-based index)
    absolute_path: Optional[bool]=None
        Whether the path to the input datasets should be stored as an absolute path
    resolution: Optional[str]=None
        Target resolution (in destination CRS units)
    bbox: Optional[Union[List[float], float]]=None
        Target bounding box as xmin,ymin,xmax,ymax (in destination CRS units)
    target_aligned_pixels: Optional[bool]=None
        Round target extent to target resolution
    input_nodata: Optional[Union[List[float], float]]=None
        Set nodata values for input bands.
    output_nodata: Optional[Union[List[float], float]]=None
        Set nodata values at the destination band level.
    hide_nodata: Optional[bool]=None
        Makes the destination band not report the NoData.
    add_alpha: Optional[bool]=None
        Adds an alpha mask band to the destination when the source raster have none.
    pixel_function: Optional[str]=None
        Specify a pixel function to calculate output value from overlapping inputs
    pixel_function_arg: Optional[Union[List[str], dict, str]]=None
        Specify argument(s) to pass to the pixel function
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def neighbors(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    kernel: List[str] | dict | str,
    input_format: List[str] | dict | str | None = None,
    open_option: List[str] | dict | str | None = None,
    quiet: bool | None = None,
    output_format: str | None = None,
    creation_option: List[str] | dict | str | None = None,
    overwrite: bool | None = None,
    append: bool | None = None,
    band: int | None = None,
    method: List[str] | dict | str | None = None,
    size: int | None = None,
    output_data_type: str | None = None,
    nodata: str | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Compute the value of each pixel from its neighbors (focal statistics)

    Consult https://gdal.org/programs/gdal_raster_neighbors.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input raster datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    kernel: Union[List[str], dict, str]
        Convolution kernel(s) to apply
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format ("GDALG" allowed)
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    append: Optional[bool]=None
        Append as a subdataset to existing output
    band: Optional[int]=None
        Input band (1-based index)
    method: Optional[Union[List[str], dict, str]]=None
        Method to combine weighed source pixels
    size: Optional[int]=None
        Neighborhood size
    output_data_type: Optional[str]=None
        Aliases: datatype
        Output data type
    nodata: Optional[str]=None
        Assign a specified nodata value to output bands ('none', numeric value, 'nan', 'inf', '-inf')
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def nodata_to_alpha(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    input_format: List[str] | dict | str | None = None,
    open_option: List[str] | dict | str | None = None,
    quiet: bool | None = None,
    output_format: str | None = None,
    creation_option: List[str] | dict | str | None = None,
    overwrite: bool | None = None,
    append: bool | None = None,
    nodata: List[float] | float | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Replace nodata value(s) with an alpha band.

    Consult https://gdal.org/programs/gdal_raster_nodata_to_alpha.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input raster datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format ("GDALG" allowed)
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    append: Optional[bool]=None
        Append as a subdataset to existing output
    nodata: Optional[Union[List[float], float]]=None
        Override nodata value of input band(s) (numeric value, 'nan', 'inf', '-inf')
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def pansharpen(
    spectral: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    input_format: List[str] | dict | str | None = None,
    open_option: List[str] | dict | str | None = None,
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]] | None = None,
    quiet: bool | None = None,
    output_format: str | None = None,
    creation_option: List[str] | dict | str | None = None,
    overwrite: bool | None = None,
    append: bool | None = None,
    resampling: str | None = None,
    weights: List[float] | float | None = None,
    nodata: float | None = None,
    bit_depth: int | None = None,
    spatial_extent_adjustment: str | None = None,
    num_threads: str | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Perform a pansharpen operation.

    Consult https://gdal.org/programs/gdal_raster_pansharpen.html for more details.

    Parameters
    ----------
    spectral: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input spectral band dataset
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Aliases: panchromatic
        Input panchromatic raster dataset
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format ("GDALG" allowed)
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    append: Optional[bool]=None
        Append as a subdataset to existing output
    resampling: Optional[str]=None
        Resampling algorithm
    weights: Optional[Union[List[float], float]]=None
        Weight for each input spectral band
    nodata: Optional[float]=None
        Override nodata value of input bands
    bit_depth: Optional[int]=None
        Override bit depth of input bands
    spatial_extent_adjustment: Optional[str]=None
        Select behavior when bands have not the same extent
    num_threads: Optional[str]=None
        Number of jobs (or ALL_CPUS)
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def pipeline(
    pipeline: str,
    input_format: List[str] | dict | str | None = None,
    open_option: List[str] | dict | str | None = None,
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]] | None = None,
    quiet: bool | None = None,
    output_format: str | None = None,
    output: osgeo.gdal.Dataset | str | os.PathLike[str] | None = None,
    creation_option: List[str] | dict | str | None = None,
    overwrite: bool | None = None,
    append: bool | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Process a raster dataset applying several steps.

    Consult https://gdal.org/programs/gdal_raster_pipeline.html for more details.

    Parameters
    ----------
    pipeline: str
        Pipeline string
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    input: Optional[Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]]=None
        Input raster datasets
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format ("GDALG" allowed)
    output: Optional[Union[gdal.Dataset, str, os.PathLike[str]]]=None
        Output raster dataset
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    append: Optional[bool]=None
        Append as a subdataset to existing output
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset
    output_string: str
        Output string, in which the result is placed


    """
    ...

def pixel_info(
    output_format: str | None = None,
    open_option: List[str] | dict | str | None = None,
    input_format: List[str] | dict | str | None = None,
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]] | None = None,
    position_dataset: osgeo.gdal.Dataset | str | os.PathLike[str] | None = None,
    input_layer: List[str] | dict | str | None = None,
    output: osgeo.gdal.Dataset | str | os.PathLike[str] | None = None,
    creation_option: List[str] | dict | str | None = None,
    layer_creation_option: List[str] | dict | str | None = None,
    overwrite: bool | None = None,
    band: List[int] | int | None = None,
    overview: int | None = None,
    position: List[float] | float | None = None,
    position_crs: str | None = None,
    resampling: str | None = None,
    promote_pixel_value_to_z: bool | None = None,
    include_field: List[str] | dict | str | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Return information on a pixel of a raster dataset.

    Consult https://gdal.org/programs/gdal_raster_pixel_info.html for more details.

    Parameters
    ----------
    output_format: Optional[str]=None
        Aliases: format
        Output format (default is 'GeoJSON' if 'position-dataset' not specified)
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Aliases: dataset
        Input raster datasets
    position_dataset: Optional[Union[gdal.Dataset, str, os.PathLike[str]]]=None
        Vector dataset with coordinates
    input_layer: Optional[Union[List[str], dict, str]]=None
        Aliases: layer
        Input layer name
    output: Optional[Union[gdal.Dataset, str, os.PathLike[str]]]=None
        Output vector dataset
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    layer_creation_option: Optional[Union[List[str], dict, str]]=None
        Layer creation option
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    band: Optional[Union[List[int], int]]=None
        Input band(s) (1-based index)
    overview: Optional[int]=None
        Which overview level of source file must be used
    position: Optional[Union[List[float], float]]=None
        Pixel position
    position_crs: Optional[str]=None
        CRS of position (default is 'pixel' if 'position-dataset' not specified)
    resampling: Optional[str]=None
        Resampling algorithm for interpolation
    promote_pixel_value_to_z: Optional[bool]=None
        Whether to set the pixel value as Z component of GeoJSON geometry
    include_field: Optional[Union[List[str], dict, str]]=None
        Fields from coordinate dataset to include in output (special values: ALL and NONE)
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

def polygonize(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    quiet: bool | None = None,
    input_format: List[str] | dict | str | None = None,
    open_option: List[str] | dict | str | None = None,
    output_format: str | None = None,
    output_open_option: List[str] | dict | str | None = None,
    creation_option: List[str] | dict | str | None = None,
    layer_creation_option: List[str] | dict | str | None = None,
    overwrite: bool | None = None,
    update: bool | None = None,
    overwrite_layer: bool | None = None,
    append: bool | None = None,
    output_layer: str | None = None,
    band: int | None = None,
    attribute_name: str | None = None,
    connect_diagonal_pixels: bool | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Create a polygon feature dataset from a raster band.

    Consult https://gdal.org/programs/gdal_raster_polygonize.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input raster datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output vector dataset
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    output_format: Optional[str]=None
        Aliases: format
        Output format ("GDALG" allowed)
    output_open_option: Optional[Union[List[str], dict, str]]=None
        Aliases: output_oo
        Output open options
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    layer_creation_option: Optional[Union[List[str], dict, str]]=None
        Layer creation option
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    update: Optional[bool]=None
        Whether to open existing dataset in update mode
    overwrite_layer: Optional[bool]=None
        Whether overwriting existing output layer is allowed
    append: Optional[bool]=None
        Whether appending to existing layer is allowed
    output_layer: Optional[str]=None
        Output layer name
    band: Optional[int]=None
        Input band (1-based index)
    attribute_name: Optional[str]=None
        Name of the field with the pixel value
    connect_diagonal_pixels: Optional[bool]=None
        Consider diagonal pixels as connected
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output vector dataset


    """
    ...

def proximity(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    input_format: List[str] | dict | str | None = None,
    open_option: List[str] | dict | str | None = None,
    quiet: bool | None = None,
    output_format: str | None = None,
    creation_option: List[str] | dict | str | None = None,
    overwrite: bool | None = None,
    append: bool | None = None,
    output_data_type: str | None = None,
    band: int | None = None,
    target_values: List[float] | float | None = None,
    distance_units: str | None = None,
    max_distance: float | None = None,
    fixed_value: float | None = None,
    nodata: float | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Produces a raster proximity map.

    Consult https://gdal.org/programs/gdal_raster_proximity.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input raster datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format ("GDALG" allowed)
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    append: Optional[bool]=None
        Append as a subdataset to existing output
    output_data_type: Optional[str]=None
        Aliases: datatype
        Output data type
    band: Optional[int]=None
        Input band (1-based index)
    target_values: Optional[Union[List[float], float]]=None
        Target pixel values
    distance_units: Optional[str]=None
        Distance units
    max_distance: Optional[float]=None
        Maximum distance. The nodata value will be used for pixels beyond this distance
    fixed_value: Optional[float]=None
        Fixed value for the pixels that are within the maximum distance (instead of the actual distance)
    nodata: Optional[float]=None
        Specify a nodata value to use for pixels that are beyond the maximum distance
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def reclassify(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    mapping: str,
    input_format: List[str] | dict | str | None = None,
    open_option: List[str] | dict | str | None = None,
    quiet: bool | None = None,
    output_format: str | None = None,
    creation_option: List[str] | dict | str | None = None,
    overwrite: bool | None = None,
    append: bool | None = None,
    output_data_type: str | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Reclassify values in a raster dataset

    Consult https://gdal.org/programs/gdal_raster_reclassify.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input raster datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    mapping: str
        Reclassification mappings (or specify a @<filename> to point to a file containing mappings
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format ("GDALG" allowed)
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    append: Optional[bool]=None
        Append as a subdataset to existing output
    output_data_type: Optional[str]=None
        Aliases: datatype
        Output data type
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def reproject(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    input_format: List[str] | dict | str | None = None,
    open_option: List[str] | dict | str | None = None,
    quiet: bool | None = None,
    output_format: str | None = None,
    creation_option: List[str] | dict | str | None = None,
    overwrite: bool | None = None,
    append: bool | None = None,
    input_crs: str | None = None,
    like: osgeo.gdal.Dataset | str | os.PathLike[str] | None = None,
    output_crs: str | None = None,
    resampling: str | None = None,
    resolution: List[float] | float | None = None,
    size: List[int] | int | None = None,
    bbox: List[float] | float | None = None,
    bbox_crs: str | None = None,
    target_aligned_pixels: bool | None = None,
    input_nodata: List[str] | dict | str | None = None,
    output_nodata: List[str] | dict | str | None = None,
    add_alpha: bool | None = None,
    warp_option: List[str] | dict | str | None = None,
    transform_option: List[str] | dict | str | None = None,
    error_threshold: float | None = None,
    num_threads: str | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Reproject a raster dataset.

    Consult https://gdal.org/programs/gdal_raster_reproject.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input raster datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format ("GDALG" allowed)
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    append: Optional[bool]=None
        Append as a subdataset to existing output
    input_crs: Optional[str]=None
        Input CRS
    like: Optional[Union[gdal.Dataset, str, os.PathLike[str]]]=None
        Dataset to use as a template for target bounds, CRS, size and nodata
    output_crs: Optional[str]=None
        Output CRS
    resampling: Optional[str]=None
        Resampling method
    resolution: Optional[Union[List[float], float]]=None
        Target resolution (in destination CRS units)
    size: Optional[Union[List[int], int]]=None
        Target size in pixels
    bbox: Optional[Union[List[float], float]]=None
        Target bounding box (in destination CRS units)
    bbox_crs: Optional[str]=None
        CRS of target bounding box
    target_aligned_pixels: Optional[bool]=None
        Round target extent to target resolution
    input_nodata: Optional[Union[List[str], dict, str]]=None
        Set nodata values for input bands ('None' to unset).
    output_nodata: Optional[Union[List[str], dict, str]]=None
        Set nodata values for output bands ('None' to unset).
    add_alpha: Optional[bool]=None
        Adds an alpha mask band to the destination when the source raster have none.
    warp_option: Optional[Union[List[str], dict, str]]=None
        Warping option(s)
    transform_option: Optional[Union[List[str], dict, str]]=None
        Transform option(s)
    error_threshold: Optional[float]=None
        Error threshold
    num_threads: Optional[str]=None
        Number of jobs (or ALL_CPUS)
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def resize(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    size: List[str] | dict | str,
    input_format: List[str] | dict | str | None = None,
    open_option: List[str] | dict | str | None = None,
    quiet: bool | None = None,
    output_format: str | None = None,
    creation_option: List[str] | dict | str | None = None,
    overwrite: bool | None = None,
    append: bool | None = None,
    resolution: List[float] | float | None = None,
    resampling: str | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Resize a raster dataset without changing the georeferenced extents.

    Consult https://gdal.org/programs/gdal_raster_resize.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input raster datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    size: Union[List[str], dict, str]
        Target size in pixels (or percentage if using '%' suffix)
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format ("GDALG" allowed)
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    append: Optional[bool]=None
        Append as a subdataset to existing output
    resolution: Optional[Union[List[float], float]]=None
        Target resolution (in destination CRS units)
    resampling: Optional[str]=None
        Resampling method
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def rgb_to_palette(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    input_format: List[str] | dict | str | None = None,
    open_option: List[str] | dict | str | None = None,
    quiet: bool | None = None,
    output_format: str | None = None,
    creation_option: List[str] | dict | str | None = None,
    overwrite: bool | None = None,
    append: bool | None = None,
    color_count: int | None = None,
    color_map: str | None = None,
    output_nodata: int | None = None,
    no_dither: bool | None = None,
    bit_depth: int | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Convert a RGB image into a pseudo-color / paletted image.

    Consult https://gdal.org/programs/gdal_raster_rgb_to_palette.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input raster datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format ("GDALG" allowed)
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    append: Optional[bool]=None
        Append as a subdataset to existing output
    color_count: Optional[int]=None
        Select the number of colors in the generated color table
    color_map: Optional[str]=None
        Color map filename
    output_nodata: Optional[int]=None
        Output nodata value
    no_dither: Optional[bool]=None
        Disable Floyd-Steinberg dithering
    bit_depth: Optional[int]=None
        Bit depth of color palette component (8 bit causes longer computation time)
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def roughness(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    input_format: List[str] | dict | str | None = None,
    open_option: List[str] | dict | str | None = None,
    quiet: bool | None = None,
    output_format: str | None = None,
    creation_option: List[str] | dict | str | None = None,
    overwrite: bool | None = None,
    append: bool | None = None,
    band: int | None = None,
    no_edges: bool | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Generate a roughness map

    Consult https://gdal.org/programs/gdal_raster_roughness.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input raster datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format ("GDALG" allowed)
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    append: Optional[bool]=None
        Append as a subdataset to existing output
    band: Optional[int]=None
        Input band (1-based index)
    no_edges: Optional[bool]=None
        Do not try to interpolate values at dataset edges or close to nodata values
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def scale(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    input_format: List[str] | dict | str | None = None,
    open_option: List[str] | dict | str | None = None,
    quiet: bool | None = None,
    output_format: str | None = None,
    creation_option: List[str] | dict | str | None = None,
    overwrite: bool | None = None,
    append: bool | None = None,
    output_data_type: str | None = None,
    band: int | None = None,
    input_min: float | None = None,
    input_max: float | None = None,
    output_min: float | None = None,
    output_max: float | None = None,
    exponent: float | None = None,
    no_clip: bool | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Scale the values of the bands of a raster dataset.

    Consult https://gdal.org/programs/gdal_raster_scale.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input raster datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format ("GDALG" allowed)
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    append: Optional[bool]=None
        Append as a subdataset to existing output
    output_data_type: Optional[str]=None
        Aliases: datatype
        Output data type
    band: Optional[int]=None
        Select band to restrict the scaling (1-based index)
    input_min: Optional[float]=None
        Minimum value of the source range
    input_max: Optional[float]=None
        Maximum value of the source range
    output_min: Optional[float]=None
        Minimum value of the destination range
    output_max: Optional[float]=None
        Maximum value of the destination range
    exponent: Optional[float]=None
        Exponent to apply non-linear scaling with a power function
    no_clip: Optional[bool]=None
        Do not clip input values to [innput-min, input-max]
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def select(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    band: List[str] | dict | str,
    input_format: List[str] | dict | str | None = None,
    open_option: List[str] | dict | str | None = None,
    quiet: bool | None = None,
    output_format: str | None = None,
    creation_option: List[str] | dict | str | None = None,
    overwrite: bool | None = None,
    append: bool | None = None,
    exclude: bool | None = None,
    mask: str | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Select a subset of bands from a raster dataset.

    Consult https://gdal.org/programs/gdal_raster_select.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input raster datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    band: Union[List[str], dict, str]
        Band(s) (1-based index, 'mask', 'mask:<band>' or color interpretation such as 'red')
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format ("GDALG" allowed)
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    append: Optional[bool]=None
        Append as a subdataset to existing output
    exclude: Optional[bool]=None
        Exclude specified bands
    mask: Optional[str]=None
        Mask band (1-based index, 'mask', 'mask:<band>' or 'none')
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def set_type(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    input_format: List[str] | dict | str | None = None,
    open_option: List[str] | dict | str | None = None,
    quiet: bool | None = None,
    output_format: str | None = None,
    creation_option: List[str] | dict | str | None = None,
    overwrite: bool | None = None,
    append: bool | None = None,
    output_data_type: str | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Modify the data type of bands of a raster dataset.

    Consult https://gdal.org/programs/gdal_raster_set_type.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input raster datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format ("GDALG" allowed)
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    append: Optional[bool]=None
        Append as a subdataset to existing output
    output_data_type: str
        Aliases: datatype
        Output data type
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def sieve(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    input_format: List[str] | dict | str | None = None,
    open_option: List[str] | dict | str | None = None,
    quiet: bool | None = None,
    output_format: str | None = None,
    creation_option: List[str] | dict | str | None = None,
    overwrite: bool | None = None,
    append: bool | None = None,
    mask: osgeo.gdal.Dataset | str | os.PathLike[str] | None = None,
    band: int | None = None,
    size_threshold: int | None = None,
    connect_diagonal_pixels: bool | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Remove small polygons from a raster dataset.

    Consult https://gdal.org/programs/gdal_raster_sieve.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input raster datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format ("GDALG" allowed)
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    append: Optional[bool]=None
        Append as a subdataset to existing output
    mask: Optional[Union[gdal.Dataset, str, os.PathLike[str]]]=None
        Use the first band of the specified file as a validity mask (all pixels with a value other than zero will be considered suitable for inclusion in polygons)
    band: Optional[int]=None
        Input band (1-based index)
    size_threshold: Optional[int]=None
        Minimum size of polygons to keep
    connect_diagonal_pixels: Optional[bool]=None
        Consider diagonal pixels as connected
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def slope(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    input_format: List[str] | dict | str | None = None,
    open_option: List[str] | dict | str | None = None,
    quiet: bool | None = None,
    output_format: str | None = None,
    creation_option: List[str] | dict | str | None = None,
    overwrite: bool | None = None,
    append: bool | None = None,
    band: int | None = None,
    unit: str | None = None,
    xscale: float | None = None,
    yscale: float | None = None,
    gradient_alg: str | None = None,
    no_edges: bool | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Generate a slope map

    Consult https://gdal.org/programs/gdal_raster_slope.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input raster datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format ("GDALG" allowed)
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    append: Optional[bool]=None
        Append as a subdataset to existing output
    band: Optional[int]=None
        Input band (1-based index)
    unit: Optional[str]=None
        Unit in which to express slopes
    xscale: Optional[float]=None
        Ratio of vertical units to horizontal X axis units
    yscale: Optional[float]=None
        Ratio of vertical units to horizontal Y axis units
    gradient_alg: Optional[str]=None
        Algorithm used to compute terrain gradient
    no_edges: Optional[bool]=None
        Do not try to interpolate values at dataset edges or close to nodata values
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def stack(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    input_format: List[str] | dict | str | None = None,
    open_option: List[str] | dict | str | None = None,
    quiet: bool | None = None,
    output_format: str | None = None,
    creation_option: List[str] | dict | str | None = None,
    overwrite: bool | None = None,
    append: bool | None = None,
    band: List[int] | int | None = None,
    absolute_path: bool | None = None,
    resolution: str | None = None,
    bbox: List[float] | float | None = None,
    target_aligned_pixels: bool | None = None,
    input_nodata: List[float] | float | None = None,
    output_nodata: List[float] | float | None = None,
    hide_nodata: bool | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Combine together input bands into a multi-band output, either virtual (VRT) or materialized.

    Consult https://gdal.org/programs/gdal_raster_stack.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input raster datasets (or specify a @<filename> to point to a file containing filenames)
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format ("GDALG" allowed)
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    append: Optional[bool]=None
        Append as a subdataset to existing output
    band: Optional[Union[List[int], int]]=None
        Input band(s) (1-based index)
    absolute_path: Optional[bool]=None
        Whether the path to the input datasets should be stored as an absolute path
    resolution: Optional[str]=None
        Target resolution (in destination CRS units)
    bbox: Optional[Union[List[float], float]]=None
        Target bounding box as xmin,ymin,xmax,ymax (in destination CRS units)
    target_aligned_pixels: Optional[bool]=None
        Round target extent to target resolution
    input_nodata: Optional[Union[List[float], float]]=None
        Set nodata values for input bands.
    output_nodata: Optional[Union[List[float], float]]=None
        Set nodata values at the destination band level.
    hide_nodata: Optional[bool]=None
        Makes the destination band not report the NoData.
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def tile(
    output: str,
    quiet: bool | None = None,
    input_format: List[str] | dict | str | None = None,
    open_option: List[str] | dict | str | None = None,
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]] | None = None,
    output_format: str | None = None,
    creation_option: List[str] | dict | str | None = None,
    tiling_scheme: str | None = None,
    min_zoom: int | None = None,
    max_zoom: int | None = None,
    min_x: int | None = None,
    max_x: int | None = None,
    min_y: int | None = None,
    max_y: int | None = None,
    no_intersection_ok: bool | None = None,
    resampling: str | None = None,
    overview_resampling: str | None = None,
    convention: str | None = None,
    tile_size: int | None = None,
    add_alpha: bool | None = None,
    no_alpha: bool | None = None,
    output_nodata: float | None = None,
    skip_blank: bool | None = None,
    metadata: List[str] | dict | str | None = None,
    copy_src_metadata: bool | None = None,
    aux_xml: bool | None = None,
    kml: bool | None = None,
    resume: bool | None = None,
    num_threads: str | None = None,
    parallel_method: str | None = None,
    excluded_values: str | None = None,
    excluded_values_pct_threshold: float | None = None,
    nodata_values_pct_threshold: float | None = None,
    webviewer: List[str] | dict | str | None = None,
    url: str | None = None,
    title: str | None = None,
    copyright: str | None = None,
    mapml_template: str | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Generate tiles in separate files from a raster dataset.

    Consult https://gdal.org/programs/gdal_raster_tile.html for more details.

    Parameters
    ----------
    output: str
        Output directory
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Aliases: dataset
        Input raster datasets
    output_format: Optional[str]=None
        Aliases: format
        Output format
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    tiling_scheme: Optional[str]=None
        Tiling scheme
    min_zoom: Optional[int]=None
        Minimum zoom level
    max_zoom: Optional[int]=None
        Maximum zoom level
    min_x: Optional[int]=None
        Minimum tile X coordinate
    max_x: Optional[int]=None
        Maximum tile X coordinate
    min_y: Optional[int]=None
        Minimum tile Y coordinate
    max_y: Optional[int]=None
        Maximum tile Y coordinate
    no_intersection_ok: Optional[bool]=None
        Whether dataset extent not intersecting tile matrix is only a warning
    resampling: Optional[str]=None
        Resampling method for max zoom
    overview_resampling: Optional[str]=None
        Resampling method for overviews
    convention: Optional[str]=None
        Tile numbering convention: xyz (from top) or tms (from bottom)
    tile_size: Optional[int]=None
        Override default tile size
    add_alpha: Optional[bool]=None
        Whether to force adding an alpha channel
    no_alpha: Optional[bool]=None
        Whether to disable adding an alpha channel
    output_nodata: Optional[float]=None
        Output nodata value
    skip_blank: Optional[bool]=None
        Do not generate blank tiles
    metadata: Optional[Union[List[str], dict, str]]=None
        Add metadata item to output tiles
    copy_src_metadata: Optional[bool]=None
        Whether to copy metadata from source dataset
    aux_xml: Optional[bool]=None
        Generate .aux.xml sidecar files when needed
    kml: Optional[bool]=None
        Generate KML files
    resume: Optional[bool]=None
        Generate only missing files
    num_threads: Optional[str]=None
        Number of jobs (or ALL_CPUS)
    parallel_method: Optional[str]=None
        Parallelization method (thread / spawn)
    excluded_values: Optional[str]=None
        Tuples of values (e.g. <R>,<G>,<B> or (<R1>,<G1>,<B1>),(<R2>,<G2>,<B2>)) that must beignored as contributing source pixels during (average) resampling
    excluded_values_pct_threshold: Optional[float]=None
        Minimum percentage of source pixels that must be set at one of the --excluded-values to cause the excluded value to be used as the target pixel value
    nodata_values_pct_threshold: Optional[float]=None
        Minimum percentage of source pixels that must be set at one of nodata (or alpha=0 or any other way to express transparent pixelto cause the target pixel value to be transparent
    webviewer: Optional[Union[List[str], dict, str]]=None
        Web viewer to generate
    url: Optional[str]=None
        URL address where the generated tiles are going to be published
    title: Optional[str]=None
        Title of the map
    copyright: Optional[str]=None
        Copyright for the map
    mapml_template: Optional[str]=None
        Filename of a template mapml file where variables will be substituted
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------


    """
    ...

def tpi(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    input_format: List[str] | dict | str | None = None,
    open_option: List[str] | dict | str | None = None,
    quiet: bool | None = None,
    output_format: str | None = None,
    creation_option: List[str] | dict | str | None = None,
    overwrite: bool | None = None,
    append: bool | None = None,
    band: int | None = None,
    no_edges: bool | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Generate a Topographic Position Index (TPI) map

    Consult https://gdal.org/programs/gdal_raster_tpi.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input raster datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format ("GDALG" allowed)
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    append: Optional[bool]=None
        Append as a subdataset to existing output
    band: Optional[int]=None
        Input band (1-based index)
    no_edges: Optional[bool]=None
        Do not try to interpolate values at dataset edges or close to nodata values
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def tri(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    input_format: List[str] | dict | str | None = None,
    open_option: List[str] | dict | str | None = None,
    quiet: bool | None = None,
    output_format: str | None = None,
    creation_option: List[str] | dict | str | None = None,
    overwrite: bool | None = None,
    append: bool | None = None,
    band: int | None = None,
    algorithm: str | None = None,
    no_edges: bool | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Generate a Terrain Ruggedness Index (TRI) map

    Consult https://gdal.org/programs/gdal_raster_tri.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input raster datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format ("GDALG" allowed)
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    append: Optional[bool]=None
        Append as a subdataset to existing output
    band: Optional[int]=None
        Input band (1-based index)
    algorithm: Optional[str]=None
        Algorithm to compute TRI
    no_edges: Optional[bool]=None
        Do not try to interpolate values at dataset edges or close to nodata values
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def unscale(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    input_format: List[str] | dict | str | None = None,
    open_option: List[str] | dict | str | None = None,
    quiet: bool | None = None,
    output_format: str | None = None,
    creation_option: List[str] | dict | str | None = None,
    overwrite: bool | None = None,
    append: bool | None = None,
    output_data_type: str | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Convert scaled values of a raster dataset into unscaled values.

    Consult https://gdal.org/programs/gdal_raster_unscale.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input raster datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format ("GDALG" allowed)
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    append: Optional[bool]=None
        Append as a subdataset to existing output
    output_data_type: Optional[str]=None
        Aliases: datatype
        Output data type
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def update(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    quiet: bool | None = None,
    input_format: List[str] | dict | str | None = None,
    open_option: List[str] | dict | str | None = None,
    geometry: str | None = None,
    geometry_crs: str | None = None,
    resampling: str | None = None,
    warp_option: List[str] | dict | str | None = None,
    transform_option: List[str] | dict | str | None = None,
    error_threshold: float | None = None,
    no_update_overviews: bool | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Update the destination raster with the content of the input one.

    Consult https://gdal.org/programs/gdal_raster_update.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input raster datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    geometry: Optional[str]=None
        Clipping geometry (WKT or GeoJSON)
    geometry_crs: Optional[str]=None
        CRS of clipping geometry
    resampling: Optional[str]=None
        Resampling method
    warp_option: Optional[Union[List[str], dict, str]]=None
        Warping option(s)
    transform_option: Optional[Union[List[str], dict, str]]=None
        Transform option(s)
    error_threshold: Optional[float]=None
        Error threshold
    no_update_overviews: Optional[bool]=None
        Do not update existing overviews
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def viewshed(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    input_format: List[str] | dict | str | None = None,
    open_option: List[str] | dict | str | None = None,
    quiet: bool | None = None,
    output_format: str | None = None,
    creation_option: List[str] | dict | str | None = None,
    overwrite: bool | None = None,
    append: bool | None = None,
    position: List[float] | float | None = None,
    height: float | None = None,
    sd_filename: osgeo.gdal.Dataset | str | os.PathLike[str] | None = None,
    target_height: float | None = None,
    mode: str | None = None,
    max_distance: float | None = None,
    min_distance: float | None = None,
    start_angle: float | None = None,
    end_angle: float | None = None,
    high_pitch: float | None = None,
    low_pitch: float | None = None,
    curvature_coefficient: float | None = None,
    band: int | None = None,
    visible_value: float | None = None,
    invisible_value: float | None = None,
    maybe_visible_value: float | None = None,
    out_of_range_value: float | None = None,
    output_nodata: float | None = None,
    observer_spacing: int | None = None,
    num_threads: str | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Compute the viewshed of a raster dataset.

    Consult https://gdal.org/programs/gdal_raster_viewshed.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input raster datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output raster dataset
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    output_format: Optional[str]=None
        Aliases: format
        Output format ("GDALG" allowed)
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    append: Optional[bool]=None
        Append as a subdataset to existing output
    position: Optional[Union[List[float], float]]=None
        Observer position
    height: Optional[float]=None
        Observer height
    sd_filename: Optional[Union[gdal.Dataset, str, os.PathLike[str]]]=None
        Filename of standard-deviation raster
    target_height: Optional[float]=None
        Height of the target above the DEM surface in the height unit of the DEM.
    mode: Optional[str]=None
        Sets what information the output contains.
    max_distance: Optional[float]=None
        Maximum distance from observer to compute visibility. It is also used to clamp the extent of the output raster.
    min_distance: Optional[float]=None
        Mask all cells less than this distance from the observer. Must be less than 'max-distance'.
    start_angle: Optional[float]=None
        Mask all cells outside of the arc ('start-angle', 'end-angle'). Clockwise degrees from north. Also used to clamp the extent of the output raster.
    end_angle: Optional[float]=None
        Mask all cells outside of the arc ('start-angle', 'end-angle'). Clockwise degrees from north. Also used to clamp the extent of the output raster.
    high_pitch: Optional[float]=None
        Mark all cells out-of-range where the observable height would be higher than the 'high-pitch' angle from the observer. Degrees from horizontal - positive is up. Must be greater than 'low-pitch'.
    low_pitch: Optional[float]=None
        Bound observable height to be no lower than the 'low-pitch' angle from the observer. Degrees from horizontal - positive is up. Must be less than 'high-pitch'.
    curvature_coefficient: Optional[float]=None
        Coefficient to consider the effect of the curvature and refraction.
    band: Optional[int]=None
        Input band (1-based index)
    visible_value: Optional[float]=None
        Pixel value to set for visible areas
    invisible_value: Optional[float]=None
        Pixel value to set for invisible areas
    maybe_visible_value: Optional[float]=None
        Pixel value to set for potentially visible areas
    out_of_range_value: Optional[float]=None
        Pixel value to set for the cells that fall outside of the range specified by the observer location and the maximum distance
    output_nodata: Optional[float]=None
        The value to be set for the cells in the output raster that have no data.
    observer_spacing: Optional[int]=None
        Cell Spacing between observers
    num_threads: Optional[str]=None
        Number of jobs (or ALL_CPUS)
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output raster dataset


    """
    ...

def zonal_stats(
    input: List[osgeo.gdal.Dataset] | List[str] | List[os.PathLike[str]],
    output: osgeo.gdal.Dataset | str | os.PathLike[str],
    zones: osgeo.gdal.Dataset | str | os.PathLike[str],
    stat: List[str] | dict | str,
    input_format: List[str] | dict | str | None = None,
    open_option: List[str] | dict | str | None = None,
    output_format: str | None = None,
    output_open_option: List[str] | dict | str | None = None,
    creation_option: List[str] | dict | str | None = None,
    layer_creation_option: List[str] | dict | str | None = None,
    overwrite: bool | None = None,
    update: bool | None = None,
    overwrite_layer: bool | None = None,
    append: bool | None = None,
    upsert: bool | None = None,
    output_layer: str | None = None,
    skip_errors: bool | None = None,
    band: List[int] | int | None = None,
    zones_band: int | None = None,
    zones_layer: str | None = None,
    weights: osgeo.gdal.Dataset | str | os.PathLike[str] | None = None,
    weights_band: int | None = None,
    pixels: str | None = None,
    include_field: List[str] | dict | str | None = None,
    include_geom: bool | None = None,
    strategy: str | None = None,
    chunk_size: str | None = None,
    quiet: bool | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Calculate raster zonal statistics

    Consult https://gdal.org/programs/gdal_raster_zonal_stats.html for more details.

    Parameters
    ----------
    input: Union[List[gdal.Dataset], List[str], List[os.PathLike[str]]]
        Input raster datasets
    output: Union[gdal.Dataset, str, os.PathLike[str]]
        Output vector dataset
    zones: Union[gdal.Dataset, str, os.PathLike[str]]
        Dataset containing zone definitions
    stat: Union[List[str], dict, str]
        Statistic(s) to compute for each zone
    input_format: Optional[Union[List[str], dict, str]]=None
        Input formats
    open_option: Optional[Union[List[str], dict, str]]=None
        Open options
    output_format: Optional[str]=None
        Aliases: format
        Output format ("GDALG" allowed)
    output_open_option: Optional[Union[List[str], dict, str]]=None
        Aliases: output_oo
        Output open options
    creation_option: Optional[Union[List[str], dict, str]]=None
        Creation option
    layer_creation_option: Optional[Union[List[str], dict, str]]=None
        Layer creation option
    overwrite: Optional[bool]=None
        Whether overwriting existing output dataset is allowed
    update: Optional[bool]=None
        Whether to open existing dataset in update mode
    overwrite_layer: Optional[bool]=None
        Whether overwriting existing output layer is allowed
    append: Optional[bool]=None
        Whether appending to existing layer is allowed
    upsert: Optional[bool]=None
        Upsert features (implies 'append')
    output_layer: Optional[str]=None
        Output layer name
    skip_errors: Optional[bool]=None
        Skip errors when writing features
    band: Optional[Union[List[int], int]]=None
        Input band(s) (1-based index)
    zones_band: Optional[int]=None
        Band from which zones should be read
    zones_layer: Optional[str]=None
        Layer from which zones should be read
    weights: Optional[Union[gdal.Dataset, str, os.PathLike[str]]]=None
        Weighting raster dataset
    weights_band: Optional[int]=None
        Band from which weights should be read
    pixels: Optional[str]=None
        Method to determine which pixels are included in stat calculation.
    include_field: Optional[Union[List[str], dict, str]]=None
        Fields from polygon zones to include in output
    include_geom: Optional[bool]=None
        Include polygon zone geometry in the output
    strategy: Optional[str]=None
        For polygon zones, whether to iterate over input features or raster chunks
    chunk_size: Optional[str]=None
        Maximum size of raster chunks read into memory
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output: gdal.ArgDatasetValue
        Output vector dataset


    """
    ...
