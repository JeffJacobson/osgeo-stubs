# typings\osgeo\gdal\alg\raster.pyi
import osgeo.gdal
import os
from collections.abc import Callable


def pansharpen(spectral: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: osgeo.gdal.Dataset | str | os.PathLike[str], input_format: list[str] | dict | str | None = None, open_option: list[str] | dict | str | None = None, input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]] | None = None, quiet: bool | None = None, output_format: str | None = None, creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, append: bool | None = None, resampling: str | None = None, weights: list[float] | float | None = None, nodata: float | None = None, bit_depth: int | None = None, spatial_extent_adjustment: str | None = None, num_threads: str | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Perform a pansharpen operation.

       Consult https://gdal.org/programs/gdal_raster_pansharpen.html for more details.

       Parameters
       ----------
       spectral: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Input spectral band dataset
       output: Union[gdal.Dataset, str, os.PathLike[str]]
           Output raster dataset
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Aliases: panchromatic
           Input panchromatic raster dataset
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       output_format: Optional[str]=None
           Aliases: format
           Output format ("GDALG" allowed)
       creation_option: Optional[Union[list[str], dict, str]]=None
           Creation option
       overwrite: Optional[bool]=None
           Whether overwriting existing output dataset is allowed
       append: Optional[bool]=None
           Append as a subdataset to existing output
       resampling: Optional[str]=None
           Resampling algorithm
       weights: Optional[Union[list[float], float]]=None
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

 


def pipeline(pipeline: str, input_format: list[str] | dict | str | None = None, open_option: list[str] | dict | str | None = None, input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]] | None = None, quiet: bool | None = None, output_format: str | None = None, output: osgeo.gdal.Dataset | str | os.PathLike[str] | None = None, creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, append: bool | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Process a raster dataset applying several steps.

       Consult https://gdal.org/programs/gdal_raster_pipeline.html for more details.

       Parameters
       ----------
       pipeline: str
           Pipeline string
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       input: Optional[Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]]=None
           Input raster datasets
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       output_format: Optional[str]=None
           Aliases: format
           Output format ("GDALG" allowed)
       output: Optional[Union[gdal.Dataset, str, os.PathLike[str]]]=None
           Output raster dataset
       creation_option: Optional[Union[list[str], dict, str]]=None
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

 


def pixel_info(output_format: str | None = None, open_option: list[str] | dict | str | None = None, input_format: list[str] | dict | str | None = None, input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]] | None = None, position_dataset: osgeo.gdal.Dataset | str | os.PathLike[str] | None = None, input_layer: list[str] | dict | str | None = None, output: osgeo.gdal.Dataset | str | os.PathLike[str] | None = None, creation_option: list[str] | dict | str | None = None, layer_creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, band: list[int] | int | None = None, overview: int | None = None, position: list[float] | float | None = None, position_crs: str | None = None, resampling: str | None = None, promote_pixel_value_to_z: bool | None = None, include_field: list[str] | dict | str | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Return information on a pixel of a raster dataset.

       Consult https://gdal.org/programs/gdal_raster_pixel_info.html for more details.

       Parameters
       ----------
       output_format: Optional[str]=None
           Aliases: format
           Output format (default is 'GeoJSON' if 'position-dataset' not specified)
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Aliases: dataset
           Input raster datasets
       position_dataset: Optional[Union[gdal.Dataset, str, os.PathLike[str]]]=None
           Vector dataset with coordinates
       input_layer: Optional[Union[list[str], dict, str]]=None
           Aliases: layer
           Input layer name
       output: Optional[Union[gdal.Dataset, str, os.PathLike[str]]]=None
           Output vector dataset
       creation_option: Optional[Union[list[str], dict, str]]=None
           Creation option
       layer_creation_option: Optional[Union[list[str], dict, str]]=None
           Layer creation option
       overwrite: Optional[bool]=None
           Whether overwriting existing output dataset is allowed
       band: Optional[Union[list[int], int]]=None
           Input band(s) (1-based index)
       overview: Optional[int]=None
           Which overview level of source file must be used
       position: Optional[Union[list[float], float]]=None
           Pixel position
       position_crs: Optional[str]=None
           CRS of position (default is 'pixel' if 'position-dataset' not specified)
       resampling: Optional[str]=None
           Resampling algorithm for interpolation
       promote_pixel_value_to_z: Optional[bool]=None
           Whether to set the pixel value as Z component of GeoJSON geometry
       include_field: Optional[Union[list[str], dict, str]]=None
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

 


def polygonize(input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: osgeo.gdal.Dataset | str | os.PathLike[str], quiet: bool | None = None, input_format: list[str] | dict | str | None = None, open_option: list[str] | dict | str | None = None, output_format: str | None = None, output_open_option: list[str] | dict | str | None = None, creation_option: list[str] | dict | str | None = None, layer_creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, update: bool | None = None, overwrite_layer: bool | None = None, append: bool | None = None, output_layer: str | None = None, band: int | None = None, attribute_name: str | None = None, connect_diagonal_pixels: bool | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Create a polygon feature dataset from a raster band.

       Consult https://gdal.org/programs/gdal_raster_polygonize.html for more details.

       Parameters
       ----------
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Input raster datasets
       output: Union[gdal.Dataset, str, os.PathLike[str]]
           Output vector dataset
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       output_format: Optional[str]=None
           Aliases: format
           Output format ("GDALG" allowed)
       output_open_option: Optional[Union[list[str], dict, str]]=None
           Aliases: output_oo
           Output open options
       creation_option: Optional[Union[list[str], dict, str]]=None
           Creation option
       layer_creation_option: Optional[Union[list[str], dict, str]]=None
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

 


def proximity(input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: osgeo.gdal.Dataset | str | os.PathLike[str], input_format: list[str] | dict | str | None = None, open_option: list[str] | dict | str | None = None, quiet: bool | None = None, output_format: str | None = None, creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, append: bool | None = None, output_data_type: str | None = None, band: int | None = None, target_values: list[float] | float | None = None, distance_units: str | None = None, max_distance: float | None = None, fixed_value: float | None = None, nodata: float | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Produces a raster proximity map.

       Consult https://gdal.org/programs/gdal_raster_proximity.html for more details.

       Parameters
       ----------
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Input raster datasets
       output: Union[gdal.Dataset, str, os.PathLike[str]]
           Output raster dataset
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       output_format: Optional[str]=None
           Aliases: format
           Output format ("GDALG" allowed)
       creation_option: Optional[Union[list[str], dict, str]]=None
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
       target_values: Optional[Union[list[float], float]]=None
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

 


def reclassify(input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: osgeo.gdal.Dataset | str | os.PathLike[str], mapping: str, input_format: list[str] | dict | str | None = None, open_option: list[str] | dict | str | None = None, quiet: bool | None = None, output_format: str | None = None, creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, append: bool | None = None, output_data_type: str | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Reclassify values in a raster dataset

       Consult https://gdal.org/programs/gdal_raster_reclassify.html for more details.

       Parameters
       ----------
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Input raster datasets
       output: Union[gdal.Dataset, str, os.PathLike[str]]
           Output raster dataset
       mapping: str
           Reclassification mappings (or specify a @<filename> to point to a file containing mappings
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       output_format: Optional[str]=None
           Aliases: format
           Output format ("GDALG" allowed)
       creation_option: Optional[Union[list[str], dict, str]]=None
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

 


def reproject(input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: osgeo.gdal.Dataset | str | os.PathLike[str], input_format: list[str] | dict | str | None = None, open_option: list[str] | dict | str | None = None, quiet: bool | None = None, output_format: str | None = None, creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, append: bool | None = None, input_crs: str | None = None, like: osgeo.gdal.Dataset | str | os.PathLike[str] | None = None, output_crs: str | None = None, resampling: str | None = None, resolution: list[float] | float | None = None, size: list[int] | int | None = None, bbox: list[float] | float | None = None, bbox_crs: str | None = None, target_aligned_pixels: bool | None = None, input_nodata: list[str] | dict | str | None = None, output_nodata: list[str] | dict | str | None = None, add_alpha: bool | None = None, warp_option: list[str] | dict | str | None = None, transform_option: list[str] | dict | str | None = None, error_threshold: float | None = None, num_threads: str | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Reproject a raster dataset.

       Consult https://gdal.org/programs/gdal_raster_reproject.html for more details.

       Parameters
       ----------
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Input raster datasets
       output: Union[gdal.Dataset, str, os.PathLike[str]]
           Output raster dataset
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       output_format: Optional[str]=None
           Aliases: format
           Output format ("GDALG" allowed)
       creation_option: Optional[Union[list[str], dict, str]]=None
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
       resolution: Optional[Union[list[float], float]]=None
           Target resolution (in destination CRS units)
       size: Optional[Union[list[int], int]]=None
           Target size in pixels
       bbox: Optional[Union[list[float], float]]=None
           Target bounding box (in destination CRS units)
       bbox_crs: Optional[str]=None
           CRS of target bounding box
       target_aligned_pixels: Optional[bool]=None
           Round target extent to target resolution
       input_nodata: Optional[Union[list[str], dict, str]]=None
           Set nodata values for input bands ('None' to unset).
       output_nodata: Optional[Union[list[str], dict, str]]=None
           Set nodata values for output bands ('None' to unset).
       add_alpha: Optional[bool]=None
           Adds an alpha mask band to the destination when the source raster have none.
       warp_option: Optional[Union[list[str], dict, str]]=None
           Warping option(s)
       transform_option: Optional[Union[list[str], dict, str]]=None
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

 


def resize(input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: osgeo.gdal.Dataset | str | os.PathLike[str], size: list[str] | dict | str, input_format: list[str] | dict | str | None = None, open_option: list[str] | dict | str | None = None, quiet: bool | None = None, output_format: str | None = None, creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, append: bool | None = None, resolution: list[float] | float | None = None, resampling: str | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Resize a raster dataset without changing the georeferenced extents.

       Consult https://gdal.org/programs/gdal_raster_resize.html for more details.

       Parameters
       ----------
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Input raster datasets
       output: Union[gdal.Dataset, str, os.PathLike[str]]
           Output raster dataset
       size: Union[list[str], dict, str]
           Target size in pixels (or percentage if using '%' suffix)
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       output_format: Optional[str]=None
           Aliases: format
           Output format ("GDALG" allowed)
       creation_option: Optional[Union[list[str], dict, str]]=None
           Creation option
       overwrite: Optional[bool]=None
           Whether overwriting existing output dataset is allowed
       append: Optional[bool]=None
           Append as a subdataset to existing output
       resolution: Optional[Union[list[float], float]]=None
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

 


def rgb_to_palette(input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: osgeo.gdal.Dataset | str | os.PathLike[str], input_format: list[str] | dict | str | None = None, open_option: list[str] | dict | str | None = None, quiet: bool | None = None, output_format: str | None = None, creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, append: bool | None = None, color_count: int | None = None, color_map: str | None = None, output_nodata: int | None = None, no_dither: bool | None = None, bit_depth: int | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Convert a RGB image into a pseudo-color / paletted image.

       Consult https://gdal.org/programs/gdal_raster_rgb_to_palette.html for more details.

       Parameters
       ----------
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Input raster datasets
       output: Union[gdal.Dataset, str, os.PathLike[str]]
           Output raster dataset
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       output_format: Optional[str]=None
           Aliases: format
           Output format ("GDALG" allowed)
       creation_option: Optional[Union[list[str], dict, str]]=None
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

 


def roughness(input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: osgeo.gdal.Dataset | str | os.PathLike[str], input_format: list[str] | dict | str | None = None, open_option: list[str] | dict | str | None = None, quiet: bool | None = None, output_format: str | None = None, creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, append: bool | None = None, band: int | None = None, no_edges: bool | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Generate a roughness map

       Consult https://gdal.org/programs/gdal_raster_roughness.html for more details.

       Parameters
       ----------
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Input raster datasets
       output: Union[gdal.Dataset, str, os.PathLike[str]]
           Output raster dataset
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       output_format: Optional[str]=None
           Aliases: format
           Output format ("GDALG" allowed)
       creation_option: Optional[Union[list[str], dict, str]]=None
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

 


def scale(input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: osgeo.gdal.Dataset | str | os.PathLike[str], input_format: list[str] | dict | str | None = None, open_option: list[str] | dict | str | None = None, quiet: bool | None = None, output_format: str | None = None, creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, append: bool | None = None, output_data_type: str | None = None, band: int | None = None, input_min: float | None = None, input_max: float | None = None, output_min: float | None = None, output_max: float | None = None, exponent: float | None = None, no_clip: bool | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Scale the values of the bands of a raster dataset.

       Consult https://gdal.org/programs/gdal_raster_scale.html for more details.

       Parameters
       ----------
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Input raster datasets
       output: Union[gdal.Dataset, str, os.PathLike[str]]
           Output raster dataset
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       output_format: Optional[str]=None
           Aliases: format
           Output format ("GDALG" allowed)
       creation_option: Optional[Union[list[str], dict, str]]=None
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

 


def select(input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: osgeo.gdal.Dataset | str | os.PathLike[str], band: list[str] | dict | str, input_format: list[str] | dict | str | None = None, open_option: list[str] | dict | str | None = None, quiet: bool | None = None, output_format: str | None = None, creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, append: bool | None = None, exclude: bool | None = None, mask: str | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Select a subset of bands from a raster dataset.

       Consult https://gdal.org/programs/gdal_raster_select.html for more details.

       Parameters
       ----------
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Input raster datasets
       output: Union[gdal.Dataset, str, os.PathLike[str]]
           Output raster dataset
       band: Union[list[str], dict, str]
           Band(s) (1-based index, 'mask', 'mask:<band>' or color interpretation such as 'red')
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       output_format: Optional[str]=None
           Aliases: format
           Output format ("GDALG" allowed)
       creation_option: Optional[Union[list[str], dict, str]]=None
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

 


def set_type(input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: osgeo.gdal.Dataset | str | os.PathLike[str], input_format: list[str] | dict | str | None = None, open_option: list[str] | dict | str | None = None, quiet: bool | None = None, output_format: str | None = None, creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, append: bool | None = None, output_data_type: str | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Modify the data type of bands of a raster dataset.

       Consult https://gdal.org/programs/gdal_raster_set_type.html for more details.

       Parameters
       ----------
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Input raster datasets
       output: Union[gdal.Dataset, str, os.PathLike[str]]
           Output raster dataset
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       output_format: Optional[str]=None
           Aliases: format
           Output format ("GDALG" allowed)
       creation_option: Optional[Union[list[str], dict, str]]=None
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

 


def sieve(input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: osgeo.gdal.Dataset | str | os.PathLike[str], input_format: list[str] | dict | str | None = None, open_option: list[str] | dict | str | None = None, quiet: bool | None = None, output_format: str | None = None, creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, append: bool | None = None, mask: osgeo.gdal.Dataset | str | os.PathLike[str] | None = None, band: int | None = None, size_threshold: int | None = None, connect_diagonal_pixels: bool | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Remove small polygons from a raster dataset.

       Consult https://gdal.org/programs/gdal_raster_sieve.html for more details.

       Parameters
       ----------
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Input raster datasets
       output: Union[gdal.Dataset, str, os.PathLike[str]]
           Output raster dataset
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       output_format: Optional[str]=None
           Aliases: format
           Output format ("GDALG" allowed)
       creation_option: Optional[Union[list[str], dict, str]]=None
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

 


def slope(input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: osgeo.gdal.Dataset | str | os.PathLike[str], input_format: list[str] | dict | str | None = None, open_option: list[str] | dict | str | None = None, quiet: bool | None = None, output_format: str | None = None, creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, append: bool | None = None, band: int | None = None, unit: str | None = None, xscale: float | None = None, yscale: float | None = None, gradient_alg: str | None = None, no_edges: bool | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Generate a slope map

       Consult https://gdal.org/programs/gdal_raster_slope.html for more details.

       Parameters
       ----------
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Input raster datasets
       output: Union[gdal.Dataset, str, os.PathLike[str]]
           Output raster dataset
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       output_format: Optional[str]=None
           Aliases: format
           Output format ("GDALG" allowed)
       creation_option: Optional[Union[list[str], dict, str]]=None
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

 


def stack(input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: osgeo.gdal.Dataset | str | os.PathLike[str], input_format: list[str] | dict | str | None = None, open_option: list[str] | dict | str | None = None, quiet: bool | None = None, output_format: str | None = None, creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, append: bool | None = None, band: list[int] | int | None = None, absolute_path: bool | None = None, resolution: str | None = None, bbox: list[float] | float | None = None, target_aligned_pixels: bool | None = None, input_nodata: list[float] | float | None = None, output_nodata: list[float] | float | None = None, hide_nodata: bool | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Combine together input bands into a multi-band output, either virtual (VRT) or materialized.

       Consult https://gdal.org/programs/gdal_raster_stack.html for more details.

       Parameters
       ----------
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Input raster datasets (or specify a @<filename> to point to a file containing filenames)
       output: Union[gdal.Dataset, str, os.PathLike[str]]
           Output raster dataset
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       output_format: Optional[str]=None
           Aliases: format
           Output format ("GDALG" allowed)
       creation_option: Optional[Union[list[str], dict, str]]=None
           Creation option
       overwrite: Optional[bool]=None
           Whether overwriting existing output dataset is allowed
       append: Optional[bool]=None
           Append as a subdataset to existing output
       band: Optional[Union[list[int], int]]=None
           Input band(s) (1-based index)
       absolute_path: Optional[bool]=None
           Whether the path to the input datasets should be stored as an absolute path
       resolution: Optional[str]=None
           Target resolution (in destination CRS units)
       bbox: Optional[Union[list[float], float]]=None
           Target bounding box as xmin,ymin,xmax,ymax (in destination CRS units)
       target_aligned_pixels: Optional[bool]=None
           Round target extent to target resolution
       input_nodata: Optional[Union[list[float], float]]=None
           Set nodata values for input bands.
       output_nodata: Optional[Union[list[float], float]]=None
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

 


def tile(output: str, quiet: bool | None = None, input_format: list[str] | dict | str | None = None, open_option: list[str] | dict | str | None = None, input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]] | None = None, output_format: str | None = None, creation_option: list[str] | dict | str | None = None, tiling_scheme: str | None = None, min_zoom: int | None = None, max_zoom: int | None = None, min_x: int | None = None, max_x: int | None = None, min_y: int | None = None, max_y: int | None = None, no_intersection_ok: bool | None = None, resampling: str | None = None, overview_resampling: str | None = None, convention: str | None = None, tile_size: int | None = None, add_alpha: bool | None = None, no_alpha: bool | None = None, output_nodata: float | None = None, skip_blank: bool | None = None, metadata: list[str] | dict | str | None = None, copy_src_metadata: bool | None = None, aux_xml: bool | None = None, kml: bool | None = None, resume: bool | None = None, num_threads: str | None = None, parallel_method: str | None = None, excluded_values: str | None = None, excluded_values_pct_threshold: float | None = None, nodata_values_pct_threshold: float | None = None, webviewer: list[str] | dict | str | None = None, url: str | None = None, title: str | None = None, copyright: str | None = None, mapml_template: str | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Generate tiles in separate files from a raster dataset.

       Consult https://gdal.org/programs/gdal_raster_tile.html for more details.

       Parameters
       ----------
       output: str
           Output directory
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Aliases: dataset
           Input raster datasets
       output_format: Optional[str]=None
           Aliases: format
           Output format
       creation_option: Optional[Union[list[str], dict, str]]=None
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
       metadata: Optional[Union[list[str], dict, str]]=None
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
       webviewer: Optional[Union[list[str], dict, str]]=None
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

 


def tpi(input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: osgeo.gdal.Dataset | str | os.PathLike[str], input_format: list[str] | dict | str | None = None, open_option: list[str] | dict | str | None = None, quiet: bool | None = None, output_format: str | None = None, creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, append: bool | None = None, band: int | None = None, no_edges: bool | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Generate a Topographic Position Index (TPI) map

       Consult https://gdal.org/programs/gdal_raster_tpi.html for more details.

       Parameters
       ----------
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Input raster datasets
       output: Union[gdal.Dataset, str, os.PathLike[str]]
           Output raster dataset
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       output_format: Optional[str]=None
           Aliases: format
           Output format ("GDALG" allowed)
       creation_option: Optional[Union[list[str], dict, str]]=None
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

 


def tri(input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: osgeo.gdal.Dataset | str | os.PathLike[str], input_format: list[str] | dict | str | None = None, open_option: list[str] | dict | str | None = None, quiet: bool | None = None, output_format: str | None = None, creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, append: bool | None = None, band: int | None = None, algorithm: str | None = None, no_edges: bool | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Generate a Terrain Ruggedness Index (TRI) map

       Consult https://gdal.org/programs/gdal_raster_tri.html for more details.

       Parameters
       ----------
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Input raster datasets
       output: Union[gdal.Dataset, str, os.PathLike[str]]
           Output raster dataset
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       output_format: Optional[str]=None
           Aliases: format
           Output format ("GDALG" allowed)
       creation_option: Optional[Union[list[str], dict, str]]=None
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

 


def unscale(input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: osgeo.gdal.Dataset | str | os.PathLike[str], input_format: list[str] | dict | str | None = None, open_option: list[str] | dict | str | None = None, quiet: bool | None = None, output_format: str | None = None, creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, append: bool | None = None, output_data_type: str | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Convert scaled values of a raster dataset into unscaled values.

       Consult https://gdal.org/programs/gdal_raster_unscale.html for more details.

       Parameters
       ----------
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Input raster datasets
       output: Union[gdal.Dataset, str, os.PathLike[str]]
           Output raster dataset
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       output_format: Optional[str]=None
           Aliases: format
           Output format ("GDALG" allowed)
       creation_option: Optional[Union[list[str], dict, str]]=None
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

 


def update(input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: osgeo.gdal.Dataset | str | os.PathLike[str], quiet: bool | None = None, input_format: list[str] | dict | str | None = None, open_option: list[str] | dict | str | None = None, geometry: str | None = None, geometry_crs: str | None = None, resampling: str | None = None, warp_option: list[str] | dict | str | None = None, transform_option: list[str] | dict | str | None = None, error_threshold: float | None = None, no_update_overviews: bool | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Update the destination raster with the content of the input one.

       Consult https://gdal.org/programs/gdal_raster_update.html for more details.

       Parameters
       ----------
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Input raster datasets
       output: Union[gdal.Dataset, str, os.PathLike[str]]
           Output raster dataset
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       geometry: Optional[str]=None
           Clipping geometry (WKT or GeoJSON)
       geometry_crs: Optional[str]=None
           CRS of clipping geometry
       resampling: Optional[str]=None
           Resampling method
       warp_option: Optional[Union[list[str], dict, str]]=None
           Warping option(s)
       transform_option: Optional[Union[list[str], dict, str]]=None
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

 


def viewshed(input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: osgeo.gdal.Dataset | str | os.PathLike[str], input_format: list[str] | dict | str | None = None, open_option: list[str] | dict | str | None = None, quiet: bool | None = None, output_format: str | None = None, creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, append: bool | None = None, position: list[float] | float | None = None, height: float | None = None, sd_filename: osgeo.gdal.Dataset | str | os.PathLike[str] | None = None, target_height: float | None = None, mode: str | None = None, max_distance: float | None = None, min_distance: float | None = None, start_angle: float | None = None, end_angle: float | None = None, high_pitch: float | None = None, low_pitch: float | None = None, curvature_coefficient: float | None = None, band: int | None = None, visible_value: float | None = None, invisible_value: float | None = None, maybe_visible_value: float | None = None, out_of_range_value: float | None = None, output_nodata: float | None = None, observer_spacing: int | None = None, num_threads: str | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Compute the viewshed of a raster dataset.

       Consult https://gdal.org/programs/gdal_raster_viewshed.html for more details.

       Parameters
       ----------
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Input raster datasets
       output: Union[gdal.Dataset, str, os.PathLike[str]]
           Output raster dataset
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       output_format: Optional[str]=None
           Aliases: format
           Output format ("GDALG" allowed)
       creation_option: Optional[Union[list[str], dict, str]]=None
           Creation option
       overwrite: Optional[bool]=None
           Whether overwriting existing output dataset is allowed
       append: Optional[bool]=None
           Append as a subdataset to existing output
       position: Optional[Union[list[float], float]]=None
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

 


def zonal_stats(input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: osgeo.gdal.Dataset | str | os.PathLike[str], zones: osgeo.gdal.Dataset | str | os.PathLike[str], stat: list[str] | dict | str, input_format: list[str] | dict | str | None = None, open_option: list[str] | dict | str | None = None, output_format: str | None = None, output_open_option: list[str] | dict | str | None = None, creation_option: list[str] | dict | str | None = None, layer_creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, update: bool | None = None, overwrite_layer: bool | None = None, append: bool | None = None, upsert: bool | None = None, output_layer: str | None = None, skip_errors: bool | None = None, band: list[int] | int | None = None, zones_band: int | None = None, zones_layer: str | None = None, weights: osgeo.gdal.Dataset | str | os.PathLike[str] | None = None, weights_band: int | None = None, pixels: str | None = None, include_field: list[str] | dict | str | None = None, include_geom: bool | None = None, strategy: str | None = None, chunk_size: str | None = None, quiet: bool | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Calculate raster zonal statistics

       Consult https://gdal.org/programs/gdal_raster_zonal_stats.html for more details.

       Parameters
       ----------
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Input raster datasets
       output: Union[gdal.Dataset, str, os.PathLike[str]]
           Output vector dataset
       zones: Union[gdal.Dataset, str, os.PathLike[str]]
           Dataset containing zone definitions
       stat: Union[list[str], dict, str]
           Statistic(s) to compute for each zone
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       output_format: Optional[str]=None
           Aliases: format
           Output format ("GDALG" allowed)
       output_open_option: Optional[Union[list[str], dict, str]]=None
           Aliases: output_oo
           Output open options
       creation_option: Optional[Union[list[str], dict, str]]=None
           Creation option
       layer_creation_option: Optional[Union[list[str], dict, str]]=None
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
       band: Optional[Union[list[int], int]]=None
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
       include_field: Optional[Union[list[str], dict, str]]=None
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

 


