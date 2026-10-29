# typings\osgeo\gdal\alg\driver\gti.pyi
import osgeo.gdal
import os
from collections.abc import Callable


def create(input: list[osgeo.gdal.Dataset] | list[str] | list[os.PathLike[str]], output: osgeo.gdal.Dataset | str | os.PathLike[str], quiet: bool | None = None, output_format: str | None = None, creation_option: list[str] | dict | str | None = None, layer_creation_option: list[str] | dict | str | None = None, overwrite: bool | None = None, update: bool | None = None, overwrite_layer: bool | None = None, append: bool | None = None, output_layer: str | None = None, recursive: bool | None = None, filename_filter: list[str] | dict | str | None = None, min_pixel_size: float | None = None, max_pixel_size: float | None = None, location_name: str | None = None, absolute_path: bool | None = None, output_crs: str | None = None, metadata: list[str] | dict | str | None = None, skip_errors: bool | None = None, profile: str | None = None, base_url: str | None = None, id_method: str | None = None, id_metadata_item: str | None = None, xml_filename: str | None = None, resolution: list[float] | float | None = None, bbox: list[float] | float | None = None, output_data_type: str | None = None, band_count: int | None = None, nodata: list[float] | float | None = None, color_interpretation: list[str] | dict | str | None = None, mask: bool | None = None, fetch_metadata: list[str] | dict | str | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> ...:
    """Create an index of raster datasets compatible of the GDAL Tile Index (GTI) driver.

       Consult https://gdal.org/programs/gdal_driver_gti_create.html for more details.

       Parameters
       ----------
       input: Union[list[gdal.Dataset], list[str], list[os.PathLike[str]]]
           Input raster datasets
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
       metadata: Optional[Union[list[str], dict, str]]=None
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
       xml_filename: Optional[str]=None
           Filename of the XML Virtual Tile Index file to generate, that can be used as an input for the GDAL GTI / Virtual Raster Tile Index driver
       resolution: Optional[Union[list[float], float]]=None
           Resolution (in destination CRS units) of the virtual mosaic
       bbox: Optional[Union[list[float], float]]=None
           Bounding box (in destination CRS units) of the virtual mosaic
       output_data_type: Optional[str]=None
           Aliases: datatype
           Datatype of the virtual mosaic
       band_count: Optional[int]=None
           Number of bands of the virtual mosaic
       nodata: Optional[Union[list[float], float]]=None
           Nodata value(s) of the bands of the virtual mosaic
       color_interpretation: Optional[Union[list[str], dict, str]]=None
           Color interpretation(s) of the bands of the virtual mosaic
       mask: Optional[bool]=None
           Defines that the virtual mosaic has a mask band
       fetch_metadata: Optional[Union[list[str], dict, str]]=None
           Fetch a metadata item from source rasters and write it as a field in the index.
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------
       output: gdal.ArgDatasetValue
           Output vector dataset


    """
    ...

 


