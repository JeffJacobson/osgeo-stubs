# typings\osgeo\gdal\alg\vector.pyi
import osgeo.gdal
import os
from collections.abc import Callable


def index(input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: osgeo.gdal.Dataset | str | os.PathLike[str], quiet: bool | None = None, output_format: str | None = None, creation_option: list[str] | dict | str | None = None, layer_creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, update: bool | None = None, overwrite_layer: bool | None = None, append: bool | None = None, output_layer: str | None = None, recursive: bool | None = None, filename_filter: list[str] | dict | str | None = None, location_name: str | None = None, absolute_path: bool | None = None, output_crs: str | None = None, metadata: list[str] | dict | str | None = None, source_crs_field_name: str | None = None, source_crs_format: str | None = None, source_layer_name: list[str] | dict | str | None = None, source_layer_index: list[int] | int | None = None, accept_different_crs: bool | None = None, accept_different_schemas: bool | None = None, dataset_name_only: bool | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Create a vector index of vector datasets.

       Consult https://gdal.org/programs/gdal_vector_index.html for more details.

       Parameters
       ----------
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Input vector datasets
       output: Union[gdal.Dataset, str, os.PathLike[str]]
           Output vector dataset
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       output_format: Optional[str]=None
           Aliases: format
           Output format
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
       recursive: Optional[bool]=None
           Whether input directories should be explored recursively.
       filename_filter: Optional[Union[list[str], dict, str]]=None
           Pattern that the filenames in input directories should follow ('*' and '?' wildcard)
       location_name: Optional[str]=None
           Name of the field with the vector path
       absolute_path: Optional[bool]=None
           Whether the path to the input datasets should be stored as an absolute path
       output_crs: Optional[str]=None
           Output CRS
       metadata: Optional[Union[list[str], dict, str]]=None
           Add dataset metadata item
       source_crs_field_name: Optional[str]=None
           Name of the field to store the CRS of each dataset
       source_crs_format: Optional[str]=None
           Format in which the CRS of each dataset must be written
       source_layer_name: Optional[Union[list[str], dict, str]]=None
           Add layer of specified name from each source file in the tile index
       source_layer_index: Optional[Union[list[int], int]]=None
           Add layer of specified index (0-based) from each source file in the tile index
       accept_different_crs: Optional[bool]=None
           Whether layers with different CRS are accepted
       accept_different_schemas: Optional[bool]=None
           Whether layers with different schemas are accepted
       dataset_name_only: Optional[bool]=None
           Whether to write the dataset name only, instead of suffixed with the layer index
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------
       output: gdal.ArgDatasetValue
           Output vector dataset


    """
    ...

 


def info(output_format: str | None = None, open_option: list[str] | dict | str | None = None, input_format: list[str] | dict | str | None = None, input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]] | None = None, input_layer: list[str] | dict | str | None = None, features: bool | None = None, summary: bool | None = None, limit: int | None = None, sql: str | None = None, where: str | None = None, fid: int | None = None, dialect: str | None = None, crs_format: str | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Return information on a vector dataset.

       Consult https://gdal.org/programs/gdal_vector_info.html for more details.

       Parameters
       ----------
       output_format: Optional[str]=None
           Aliases: format
           Output format
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Aliases: dataset
           Input vector datasets
       input_layer: Optional[Union[list[str], dict, str]]=None
           Aliases: layer
           Input layer name
       features: Optional[bool]=None
           list all features (beware of RAM consumption on large layers)
       summary: Optional[bool]=None
           list the layer names and the geometry type
       limit: Optional[int]=None
           Limit the number of features per layer (implies --features)
       sql: Optional[str]=None
           Execute the indicated SQL statement and return the result
       where: Optional[str]=None
           Attribute query in a restricted form of the queries used in the SQL WHERE statement
       fid: Optional[int]=None
           Feature identifier
       dialect: Optional[str]=None
           SQL dialect
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

 


def layer_algebra(operation: str, input: osgeo.gdal.Dataset | str | os.PathLike[str], method: osgeo.gdal.Dataset | str | os.PathLike[str], output: osgeo.gdal.Dataset | str | os.PathLike[str], quiet: bool | None = None, output_format: str | None = None, open_option: list[str] | dict | str | None = None, input_format: list[str] | dict | str | None = None, creation_option: list[str] | dict | str | None = None, layer_creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, update: bool | None = None, overwrite_layer: bool | None = None, append: bool | None = None, input_layer: str | None = None, method_layer: str | None = None, output_layer: str | None = None, geometry_type: str | None = None, input_prefix: str | None = None, input_field: list[str] | dict | str | None = None, no_input_field: bool | None = None, all_input_field: bool | None = None, method_prefix: str | None = None, method_field: list[str] | dict | str | None = None, no_method_field: bool | None = None, all_method_field: bool | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Perform algebraic operation between 2 layers.

       Consult https://gdal.org/programs/gdal_vector_layer_algebra.html for more details.

       Parameters
       ----------
       operation: str
           Operation to perform
       input: Union[gdal.Dataset, str, os.PathLike[str]]
           Input vector dataset
       method: Union[gdal.Dataset, str, os.PathLike[str]]
           Method vector dataset
       output: Union[gdal.Dataset, str, os.PathLike[str]]
           Output vector dataset
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
       input_layer: Optional[str]=None
           Input layer name
       method_layer: Optional[str]=None
           Method layer name
       output_layer: Optional[str]=None
           Output layer name
       geometry_type: Optional[str]=None
           Geometry type
       input_prefix: Optional[str]=None
           Prefix for fields corresponding to input layer
       input_field: Optional[Union[list[str], dict, str]]=None
           Input field(s) to add to output layer
       no_input_field: Optional[bool]=None
           Do not add any input field to output layer
       all_input_field: Optional[bool]=None
           Add all input fields to output layer
       method_prefix: Optional[str]=None
           Prefix for fields corresponding to method layer
       method_field: Optional[Union[list[str], dict, str]]=None
           Method field(s) to add to output layer
       no_method_field: Optional[bool]=None
           Do not add any method field to output layer
       all_method_field: Optional[bool]=None
           Add all method fields to output layer
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------
       output: gdal.ArgDatasetValue
           Output vector dataset


    """
    ...

 


def make_point(input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: osgeo.gdal.Dataset | str | os.PathLike[str], x: str, y: str, input_format: list[str] | dict | str | None = None, open_option: list[str] | dict | str | None = None, input_layer: list[str] | dict | str | None = None, quiet: bool | None = None, output_format: str | None = None, output_open_option: list[str] | dict | str | None = None, creation_option: list[str] | dict | str | None = None, layer_creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, update: bool | None = None, overwrite_layer: bool | None = None, append: bool | None = None, upsert: bool | None = None, output_layer: str | None = None, skip_errors: bool | None = None, z: str | None = None, m: str | None = None, output_crs: str | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Create point geometries from attribute fields

       Consult https://gdal.org/programs/gdal_vector_make_point.html for more details.

       Parameters
       ----------
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Input vector datasets
       output: Union[gdal.Dataset, str, os.PathLike[str]]
           Output vector dataset
       x: str
           Field from which X coordinate should be read
       y: str
           Field from which Y coordinate should be read
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       input_layer: Optional[Union[list[str], dict, str]]=None
           Aliases: layer
           Input layer name(s)
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
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
       z: Optional[str]=None
           Optional field from which Z coordinate should be read
       m: Optional[str]=None
           Optional field from which M coordinate should be read
       output_crs: Optional[str]=None
           Output CRS
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------
       output: gdal.ArgDatasetValue
           Output vector dataset


    """
    ...

 


def make_valid(input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: osgeo.gdal.Dataset | str | os.PathLike[str], input_format: list[str] | dict | str | None = None, open_option: list[str] | dict | str | None = None, input_layer: list[str] | dict | str | None = None, quiet: bool | None = None, output_format: str | None = None, output_open_option: list[str] | dict | str | None = None, creation_option: list[str] | dict | str | None = None, layer_creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, update: bool | None = None, overwrite_layer: bool | None = None, append: bool | None = None, upsert: bool | None = None, output_layer: str | None = None, skip_errors: bool | None = None, active_layer: str | None = None, active_geometry: str | None = None, method: str | None = None, keep_lower_dim: bool | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Fix validity of geometries of a vector dataset.

       Consult https://gdal.org/programs/gdal_vector_make_valid.html for more details.

       Parameters
       ----------
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Input vector datasets
       output: Union[gdal.Dataset, str, os.PathLike[str]]
           Output vector dataset
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       input_layer: Optional[Union[list[str], dict, str]]=None
           Aliases: layer
           Input layer name(s)
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
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
       active_layer: Optional[str]=None
           Set active layer (if not specified, all)
       active_geometry: Optional[str]=None
           Geometry field name to which to restrict the processing (if not specified, all)
       method: Optional[str]=None
           Algorithm to use when repairing invalid geometries.
       keep_lower_dim: Optional[bool]=None
           Keep components of lower dimension after MakeValid()
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------
       output: gdal.ArgDatasetValue
           Output vector dataset


    """
    ...

 


def partition(input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: str, input_format: list[str] | dict | str | None = None, open_option: list[str] | dict | str | None = None, quiet: bool | None = None, overwrite: bool | None = None, append: bool | None = None, output_format: str | None = None, creation_option: list[str] | dict | str | None = None, layer_creation_option: list[str] | dict | str | None = None, field: list[str] | dict | str | None = None, scheme: str | None = None, pattern: str | None = None, feature_limit: int | None = None, max_file_size: str | None = None, omit_partitioned_field: bool | None = None, skip_errors: bool | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Partition a vector dataset into multiple files.

       Consult https://gdal.org/programs/gdal_vector_partition.html for more details.

       Parameters
       ----------
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Input vector datasets
       output: str
           Output directory
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       overwrite: Optional[bool]=None
           Whether overwriting existing output dataset is allowed
       append: Optional[bool]=None
           Whether appending to existing layer is allowed
       output_format: Optional[str]=None
           Aliases: format
           Output format
       creation_option: Optional[Union[list[str], dict, str]]=None
           Creation option
       layer_creation_option: Optional[Union[list[str], dict, str]]=None
           Layer creation option
       field: Optional[Union[list[str], dict, str]]=None
           Attribute or geometry field(s) on which to partition
       scheme: Optional[str]=None
           Partitioning scheme
       pattern: Optional[str]=None
           Filename pattern ('part_%010d' for scheme=hive, '{LAYER_NAME}_{FIELD_VALUE}_%010d' for scheme=flat)
       feature_limit: Optional[int]=None
           Maximum number of features per file
       max_file_size: Optional[str]=None
           Maximum file size (MB or GB suffix can be used)
       omit_partitioned_field: Optional[bool]=None
           Whether to omit partitioned fields from target layer definition
       skip_errors: Optional[bool]=None
           Skip errors when writing features
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------


    """
    ...

 


def pipeline(pipeline: str, input_format: list[str] | dict | str | None = None, open_option: list[str] | dict | str | None = None, input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]] | None = None, input_layer: list[str] | dict | str | None = None, quiet: bool | None = None, output_format: str | None = None, output_open_option: list[str] | dict | str | None = None, output: osgeo.gdal.Dataset | str | os.PathLike[str] | None = None, creation_option: list[str] | dict | str | None = None, layer_creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, update: bool | None = None, overwrite_layer: bool | None = None, append: bool | None = None, upsert: bool | None = None, output_layer: str | None = None, skip_errors: bool | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Process a vector dataset applying several steps.

       Consult https://gdal.org/programs/gdal_vector_pipeline.html for more details.

       Parameters
       ----------
       pipeline: str
           Pipeline string
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       input: Optional[Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]]=None
           Input vector datasets
       input_layer: Optional[Union[list[str], dict, str]]=None
           Aliases: layer
           Input layer name(s)
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       output_format: Optional[str]=None
           Aliases: format
           Output format ("GDALG" allowed)
       output_open_option: Optional[Union[list[str], dict, str]]=None
           Aliases: output_oo
           Output open options
       output: Optional[Union[gdal.Dataset, str, os.PathLike[str]]]=None
           Output vector dataset
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

 


def rasterize(input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: osgeo.gdal.Dataset | str | os.PathLike[str], quiet: bool | None = None, output_format: str | None = None, open_option: list[str] | dict | str | None = None, input_format: list[str] | dict | str | None = None, creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, band: list[int] | int | None = None, invert: bool | None = None, all_touched: bool | None = None, burn: list[float] | float | None = None, attribute_name: str | None = None, _3d: bool | None = None, input_layer: str | None = None, where: str | None = None, sql: str | None = None, dialect: str | None = None, nodata: float | None = None, init: list[float] | float | None = None, crs: str | None = None, transformer_option: list[str] | dict | str | None = None, extent: list[float] | float | None = None, resolution: list[float] | float | None = None, target_aligned_pixels: bool | None = None, size: list[int] | int | None = None, output_data_type: str | None = None, optimization: str | None = None, add: bool | None = None, update: bool | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Burns vector geometries into a raster.

       Consult https://gdal.org/programs/gdal_vector_rasterize.html for more details.

       Parameters
       ----------
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Input vector datasets
       output: Union[gdal.Dataset, str, os.PathLike[str]]
           Output raster dataset
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
       band: Optional[Union[list[int], int]]=None
           The band(s) to burn values into (1-based index)
       invert: Optional[bool]=None
           Invert the rasterization
       all_touched: Optional[bool]=None
           Enables the ALL_TOUCHED rasterization option
       burn: Optional[Union[list[float], float]]=None
           Burn value
       attribute_name: Optional[str]=None
           Attribute name
       _3d: Optional[bool]=None
           Indicates that a burn value should be extracted from the Z values of the feature
       input_layer: Optional[str]=None
           Input layer name
       where: Optional[str]=None
           SQL where clause
       sql: Optional[str]=None
           SQL select statement
       dialect: Optional[str]=None
           SQL dialect
       nodata: Optional[float]=None
           Assign a specified nodata value to output bands
       init: Optional[Union[list[float], float]]=None
           Pre-initialize output bands with specified value
       crs: Optional[str]=None
           Override the projection for the output file
       transformer_option: Optional[Union[list[str], dict, str]]=None
           Set a transformer option suitable to pass to GDALCreateGenImgProjTransformer2
       extent: Optional[Union[list[float], float]]=None
           Set the target georeferenced extent
       resolution: Optional[Union[list[float], float]]=None
           Set the target resolution
       target_aligned_pixels: Optional[bool]=None
           (target aligned pixels) Align the coordinates of the extent of the output file to the values of the resolution
       size: Optional[Union[list[int], int]]=None
           Set the target size in pixels and lines
       output_data_type: Optional[str]=None
           Aliases: datatype
           Output data type
       optimization: Optional[str]=None
           Force the algorithm used (results are identical)
       add: Optional[bool]=None
           Add to existing raster
       update: Optional[bool]=None
           Whether to open existing dataset in update mode
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------
       output: gdal.ArgDatasetValue
           Output raster dataset


    """
    ...

 


def rename_layer(input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: osgeo.gdal.Dataset | str | os.PathLike[str], input_format: list[str] | dict | str | None = None, open_option: list[str] | dict | str | None = None, quiet: bool | None = None, output_format: str | None = None, output_open_option: list[str] | dict | str | None = None, creation_option: list[str] | dict | str | None = None, layer_creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, update: bool | None = None, overwrite_layer: bool | None = None, append: bool | None = None, upsert: bool | None = None, output_layer: str | None = None, skip_errors: bool | None = None, input_layer: str | None = None, ascii: bool | None = None, lower_case: bool | None = None, filename_compatible: bool | None = None, reserved_characters: str | None = None, replacement_character: str | None = None, max_length: int | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Rename layer(s) of a vector dataset.

       Consult https://gdal.org/programs/gdal_vector_rename_layer.html for more details.

       Parameters
       ----------
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Input vector datasets
       output: Union[gdal.Dataset, str, os.PathLike[str]]
           Output vector dataset
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
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
       input_layer: Optional[str]=None
           Input layer name
       ascii: Optional[bool]=None
           Force names to ASCII character
       lower_case: Optional[bool]=None
           Force names to lower case (only on ASCII characters)
       filename_compatible: Optional[bool]=None
           Force names to be usable as filenames
       reserved_characters: Optional[str]=None
           Reserved character(s) to be removed
       replacement_character: Optional[str]=None
           Replacement character when ASCII conversion not possible
       max_length: Optional[int]=None
           Maximum length of layer names
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------
       output: gdal.ArgDatasetValue
           Output vector dataset


    """
    ...

 


def reproject(input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: osgeo.gdal.Dataset | str | os.PathLike[str], output_crs: str, input_format: list[str] | dict | str | None = None, open_option: list[str] | dict | str | None = None, input_layer: list[str] | dict | str | None = None, quiet: bool | None = None, output_format: str | None = None, output_open_option: list[str] | dict | str | None = None, creation_option: list[str] | dict | str | None = None, layer_creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, update: bool | None = None, overwrite_layer: bool | None = None, append: bool | None = None, upsert: bool | None = None, output_layer: str | None = None, skip_errors: bool | None = None, active_layer: str | None = None, input_crs: str | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Reproject a vector dataset.

       Consult https://gdal.org/programs/gdal_vector_reproject.html for more details.

       Parameters
       ----------
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Input vector datasets
       output: Union[gdal.Dataset, str, os.PathLike[str]]
           Output vector dataset
       output_crs: str
           Output CRS
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       input_layer: Optional[Union[list[str], dict, str]]=None
           Aliases: layer
           Input layer name(s)
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
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
       active_layer: Optional[str]=None
           Set active layer (if not specified, all)
       input_crs: Optional[str]=None
           Input CRS
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------
       output: gdal.ArgDatasetValue
           Output vector dataset


    """
    ...

 


def segmentize(input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: osgeo.gdal.Dataset | str | os.PathLike[str], max_length: float, input_format: list[str] | dict | str | None = None, open_option: list[str] | dict | str | None = None, input_layer: list[str] | dict | str | None = None, quiet: bool | None = None, output_format: str | None = None, output_open_option: list[str] | dict | str | None = None, creation_option: list[str] | dict | str | None = None, layer_creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, update: bool | None = None, overwrite_layer: bool | None = None, append: bool | None = None, upsert: bool | None = None, output_layer: str | None = None, skip_errors: bool | None = None, active_layer: str | None = None, active_geometry: str | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Segmentize geometries of a vector dataset.

       Consult https://gdal.org/programs/gdal_vector_segmentize.html for more details.

       Parameters
       ----------
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Input vector datasets
       output: Union[gdal.Dataset, str, os.PathLike[str]]
           Output vector dataset
       max_length: float
           Maximum length of a segment
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       input_layer: Optional[Union[list[str], dict, str]]=None
           Aliases: layer
           Input layer name(s)
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
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
       active_layer: Optional[str]=None
           Set active layer (if not specified, all)
       active_geometry: Optional[str]=None
           Geometry field name to which to restrict the processing (if not specified, all)
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------
       output: gdal.ArgDatasetValue
           Output vector dataset


    """
    ...

 


def select(input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: osgeo.gdal.Dataset | str | os.PathLike[str], fields: list[str] | dict | str, input_format: list[str] | dict | str | None = None, open_option: list[str] | dict | str | None = None, input_layer: list[str] | dict | str | None = None, quiet: bool | None = None, output_format: str | None = None, output_open_option: list[str] | dict | str | None = None, creation_option: list[str] | dict | str | None = None, layer_creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, update: bool | None = None, overwrite_layer: bool | None = None, append: bool | None = None, upsert: bool | None = None, output_layer: str | None = None, skip_errors: bool | None = None, active_layer: str | None = None, exclude: bool | None = None, ignore_missing_fields: bool | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Select a subset of fields from a vector dataset.

       Consult https://gdal.org/programs/gdal_vector_select.html for more details.

       Parameters
       ----------
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Input vector datasets
       output: Union[gdal.Dataset, str, os.PathLike[str]]
           Output vector dataset
       fields: Union[list[str], dict, str]
           Fields to select (or exclude if --exclude)
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       input_layer: Optional[Union[list[str], dict, str]]=None
           Aliases: layer
           Input layer name(s)
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
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
       active_layer: Optional[str]=None
           Set active layer (if not specified, all)
       exclude: Optional[bool]=None
           Exclude specified fields
       ignore_missing_fields: Optional[bool]=None
           Ignore missing fields
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------
       output: gdal.ArgDatasetValue
           Output vector dataset


    """
    ...

 


def set_field_type(input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: osgeo.gdal.Dataset | str | os.PathLike[str], field_name: str, input_field_type: str, input_format: list[str] | dict | str | None = None, open_option: list[str] | dict | str | None = None, input_layer: list[str] | dict | str | None = None, quiet: bool | None = None, output_format: str | None = None, output_open_option: list[str] | dict | str | None = None, creation_option: list[str] | dict | str | None = None, layer_creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, update: bool | None = None, overwrite_layer: bool | None = None, append: bool | None = None, upsert: bool | None = None, output_layer: str | None = None, skip_errors: bool | None = None, active_layer: str | None = None, field_type: str | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Modify the type of a field of a vector dataset.

       Consult https://gdal.org/programs/gdal_vector_set_field_type.html for more details.

       Parameters
       ----------
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Input vector datasets
       output: Union[gdal.Dataset, str, os.PathLike[str]]
           Output vector dataset
       field_name: str
           Field name
       input_field_type: str
           Source field type or subtype
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       input_layer: Optional[Union[list[str], dict, str]]=None
           Aliases: layer
           Input layer name(s)
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
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
       active_layer: Optional[str]=None
           Set active layer (if not specified, all)
       field_type: str
           Aliases: output_field_type
           Target field type or subtype
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------
       output: gdal.ArgDatasetValue
           Output vector dataset


    """
    ...

 


def set_geom_type(input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: osgeo.gdal.Dataset | str | os.PathLike[str], input_format: list[str] | dict | str | None = None, open_option: list[str] | dict | str | None = None, input_layer: list[str] | dict | str | None = None, quiet: bool | None = None, output_format: str | None = None, output_open_option: list[str] | dict | str | None = None, creation_option: list[str] | dict | str | None = None, layer_creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, update: bool | None = None, overwrite_layer: bool | None = None, append: bool | None = None, upsert: bool | None = None, output_layer: str | None = None, skip_errors: bool | None = None, active_layer: str | None = None, active_geometry: str | None = None, layer_only: bool | None = None, feature_only: bool | None = None, geometry_type: str | None = None, multi: bool | None = None, single: bool | None = None, linear: bool | None = None, curve: bool | None = None, dim: str | None = None, skip: bool | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Modify the geometry type of a vector dataset.

       Consult https://gdal.org/programs/gdal_vector_set_geom_type.html for more details.

       Parameters
       ----------
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Input vector datasets
       output: Union[gdal.Dataset, str, os.PathLike[str]]
           Output vector dataset
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       input_layer: Optional[Union[list[str], dict, str]]=None
           Aliases: layer
           Input layer name(s)
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
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
       active_layer: Optional[str]=None
           Set active layer (if not specified, all)
       active_geometry: Optional[str]=None
           Geometry field name to which to restrict the processing (if not specified, all)
       layer_only: Optional[bool]=None
           Only modify the layer geometry type
       feature_only: Optional[bool]=None
           Only modify the geometry type of features
       geometry_type: Optional[str]=None
           Geometry type
       multi: Optional[bool]=None
           Force geometries to MULTI geometry types
       single: Optional[bool]=None
           Force geometries to non-MULTI geometry types
       linear: Optional[bool]=None
           Convert curve geometries to linear types
       curve: Optional[bool]=None
           Convert linear geometries to curve types
       dim: Optional[str]=None
           Force geometries to the specified dimension
       skip: Optional[bool]=None
           Skip feature when change of feature geometry type failed
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------
       output: gdal.ArgDatasetValue
           Output vector dataset


    """
    ...

 


def simplify(input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: osgeo.gdal.Dataset | str | os.PathLike[str], tolerance: float, input_format: list[str] | dict | str | None = None, open_option: list[str] | dict | str | None = None, input_layer: list[str] | dict | str | None = None, quiet: bool | None = None, output_format: str | None = None, output_open_option: list[str] | dict | str | None = None, creation_option: list[str] | dict | str | None = None, layer_creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, update: bool | None = None, overwrite_layer: bool | None = None, append: bool | None = None, upsert: bool | None = None, output_layer: str | None = None, skip_errors: bool | None = None, active_layer: str | None = None, active_geometry: str | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Simplify geometries of a vector dataset.

       Consult https://gdal.org/programs/gdal_vector_simplify.html for more details.

       Parameters
       ----------
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Input vector datasets
       output: Union[gdal.Dataset, str, os.PathLike[str]]
           Output vector dataset
       tolerance: float
           Distance tolerance for simplification.
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       input_layer: Optional[Union[list[str], dict, str]]=None
           Aliases: layer
           Input layer name(s)
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
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
       active_layer: Optional[str]=None
           Set active layer (if not specified, all)
       active_geometry: Optional[str]=None
           Geometry field name to which to restrict the processing (if not specified, all)
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------
       output: gdal.ArgDatasetValue
           Output vector dataset


    """
    ...

 


def simplify_coverage(input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: osgeo.gdal.Dataset | str | os.PathLike[str], tolerance: float, input_format: list[str] | dict | str | None = None, open_option: list[str] | dict | str | None = None, input_layer: list[str] | dict | str | None = None, quiet: bool | None = None, output_format: str | None = None, output_open_option: list[str] | dict | str | None = None, creation_option: list[str] | dict | str | None = None, layer_creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, update: bool | None = None, overwrite_layer: bool | None = None, append: bool | None = None, upsert: bool | None = None, output_layer: str | None = None, skip_errors: bool | None = None, active_layer: str | None = None, preserve_boundary: bool | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Simplify shared boundaries of a polygonal vector dataset.

       Consult https://gdal.org/programs/gdal_vector_simplify_coverage.html for more details.

       Parameters
       ----------
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Input vector datasets
       output: Union[gdal.Dataset, str, os.PathLike[str]]
           Output vector dataset
       tolerance: float
           Distance tolerance for simplification.
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       input_layer: Optional[Union[list[str], dict, str]]=None
           Aliases: layer
           Input layer name(s)
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
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
       active_layer: Optional[str]=None
           Set active layer (if not specified, all)
       preserve_boundary: Optional[bool]=None
           Whether the exterior boundary should be preserved.
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------
       output: gdal.ArgDatasetValue
           Output vector dataset


    """
    ...

 


def sort(input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: osgeo.gdal.Dataset | str | os.PathLike[str], input_format: list[str] | dict | str | None = None, open_option: list[str] | dict | str | None = None, input_layer: list[str] | dict | str | None = None, quiet: bool | None = None, output_format: str | None = None, output_open_option: list[str] | dict | str | None = None, creation_option: list[str] | dict | str | None = None, layer_creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, update: bool | None = None, overwrite_layer: bool | None = None, append: bool | None = None, upsert: bool | None = None, output_layer: str | None = None, skip_errors: bool | None = None, geometry_field: str | None = None, method: str | None = None, use_tempfile: bool | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Spatially order the features in a layer

       Consult https://gdal.org/programs/gdal_vector_sort.html for more details.

       Parameters
       ----------
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Input vector datasets
       output: Union[gdal.Dataset, str, os.PathLike[str]]
           Output vector dataset
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       input_layer: Optional[Union[list[str], dict, str]]=None
           Aliases: layer
           Input layer name(s)
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
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
       geometry_field: Optional[str]=None
           Name of geometry field to use in sort
       method: Optional[str]=None
           Geometry sorting algorithm
       use_tempfile: Optional[bool]=None
           Write features to a temporary file to avoid reading the entire input dataset into memory
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------
       output: gdal.ArgDatasetValue
           Output vector dataset


    """
    ...

 


def sql(sql: list[str] | dict | str, input_format: list[str] | dict | str | None = None, open_option: list[str] | dict | str | None = None, input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]] | None = None, quiet: bool | None = None, output_format: str | None = None, output_open_option: list[str] | dict | str | None = None, output: osgeo.gdal.Dataset | str | os.PathLike[str] | None = None, creation_option: list[str] | dict | str | None = None, layer_creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, update: bool | None = None, overwrite_layer: bool | None = None, append: bool | None = None, upsert: bool | None = None, skip_errors: bool | None = None, output_layer: list[str] | dict | str | None = None, dialect: str | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Apply SQL statement(s) to a dataset.

       Consult https://gdal.org/programs/gdal_vector_sql.html for more details.

       Parameters
       ----------
       sql: Union[list[str], dict, str]
           SQL statement(s)
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Aliases: dataset
           Input vector datasets
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       output_format: Optional[str]=None
           Aliases: format
           Output format ("GDALG" allowed)
       output_open_option: Optional[Union[list[str], dict, str]]=None
           Aliases: output_oo
           Output open options
       output: Optional[Union[gdal.Dataset, str, os.PathLike[str]]]=None
           Output vector dataset
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
       skip_errors: Optional[bool]=None
           Skip errors when writing features
       output_layer: Optional[Union[list[str], dict, str]]=None
           Output layer name(s)
       dialect: Optional[str]=None
           SQL dialect (e.g. OGRSQL, SQLITE)
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------
       output: gdal.ArgDatasetValue
           Output vector dataset


    """
    ...

 


def swap_xy(input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: osgeo.gdal.Dataset | str | os.PathLike[str], input_format: list[str] | dict | str | None = None, open_option: list[str] | dict | str | None = None, input_layer: list[str] | dict | str | None = None, quiet: bool | None = None, output_format: str | None = None, output_open_option: list[str] | dict | str | None = None, creation_option: list[str] | dict | str | None = None, layer_creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, update: bool | None = None, overwrite_layer: bool | None = None, append: bool | None = None, upsert: bool | None = None, output_layer: str | None = None, skip_errors: bool | None = None, active_layer: str | None = None, active_geometry: str | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Swap X and Y coordinates of geometries of a vector dataset.

       Consult https://gdal.org/programs/gdal_vector_swap_xy.html for more details.

       Parameters
       ----------
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Input vector datasets
       output: Union[gdal.Dataset, str, os.PathLike[str]]
           Output vector dataset
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       input_layer: Optional[Union[list[str], dict, str]]=None
           Aliases: layer
           Input layer name(s)
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
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
       active_layer: Optional[str]=None
           Set active layer (if not specified, all)
       active_geometry: Optional[str]=None
           Geometry field name to which to restrict the processing (if not specified, all)
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------
       output: gdal.ArgDatasetValue
           Output vector dataset


    """
    ...

 


def update(input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: osgeo.gdal.Dataset | str | os.PathLike[str], input_format: list[str] | dict | str | None = None, open_option: list[str] | dict | str | None = None, input_layer: list[str] | dict | str | None = None, quiet: bool | None = None, output_open_option: list[str] | dict | str | None = None, output_layer: str | None = None, mode: str | None = None, key: list[str] | dict | str | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Update an existing vector dataset with an input vector dataset.

       Consult https://gdal.org/programs/gdal_vector_update.html for more details.

       Parameters
       ----------
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Input vector datasets
       output: Union[gdal.Dataset, str, os.PathLike[str]]
           Output vector dataset
       input_format: Optional[Union[list[str], dict, str]]=None
           Input formats
       open_option: Optional[Union[list[str], dict, str]]=None
           Open options
       input_layer: Optional[Union[list[str], dict, str]]=None
           Input layer name
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       output_open_option: Optional[Union[list[str], dict, str]]=None
           Aliases: output_oo
           Output open options
       output_layer: Optional[str]=None
           Output layer name
       mode: Optional[str]=None
           Set update mode
       key: Optional[Union[list[str], dict, str]]=None
           Field(s) used as a key to identify features
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------
       output: gdal.ArgDatasetValue
           Output vector dataset


    """
    ...

 


