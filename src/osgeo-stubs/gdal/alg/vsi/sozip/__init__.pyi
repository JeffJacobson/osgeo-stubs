import os
from collections.abc import Callable
from typing import List

import osgeo.gdal
from osgeo import gdal


def create(input: List[str] | dict | str, output: str, quiet: bool | None = None, overwrite: bool | None = None, recursive: bool | None = None, no_paths: bool | None = None, enable_sozip: str | None = None, sozip_chunk_size: str | None = None, sozip_min_file_size: str | None = None, content_type: str | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> str:
    """Create a Seek-optimized ZIP (SOZIP) file.

       Consult https://gdal.org/programs/gdal_vsi_sozip.html for more details.

       Parameters
       ----------
       input: Union[List[str], dict, str]
           Input filenames
       output: str
           Output ZIP filename
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       overwrite: Optional[bool]=None
           Whether overwriting existing output dataset is allowed
       recursive: Optional[bool]=None
           Travels the directory structure of the specified directories recursively
       no_paths: Optional[bool]=None
           Aliases: junk_paths
           Store just the name of a saved file, and do not store directory names
       enable_sozip: Optional[str]=None
           Whether to automatically/systematically/never apply the SOZIP optimization
       sozip_chunk_size: Optional[str]=None
           Chunk size for a seek-optimized file
       sozip_min_file_size: Optional[str]=None
           Minimum file size to decide if a file should be seek-optimized
       content_type: Optional[str]=None
           Store the Content-Type of the file being added.
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------
       output_string: str
           Output string, in which the result is placed


    """
    ...


def list(input: str | os.PathLike[str], progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> str:
    """List content of a ZIP file, with SOZIP related information.

       Consult https://gdal.org/programs/gdal_vsi_sozip.html for more details.

       Parameters
       ----------
       input: Union[str, os.PathLike[str]]
           Input ZIP filename
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------
       output_string: str
           Output string, in which the result is placed


    """
    ...


def optimize(input: List[str] | dict | str, output: str, quiet: bool | None = None, overwrite: bool | None = None, enable_sozip: str | None = None, sozip_chunk_size: str | None = None, sozip_min_file_size: str | None = None, progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> str:
    """Create a Seek-optimized ZIP (SOZIP) file from a regular ZIP file.

       Consult https://gdal.org/programs/gdal_vsi_sozip.html for more details.

       Parameters
       ----------
       input: Union[List[str], dict, str]
           Input ZIP filename
       output: str
           Output ZIP filename
       quiet: Optional[bool]=None
           Quiet mode (no progress bar or warning message)
       overwrite: Optional[bool]=None
           Whether overwriting existing output dataset is allowed
       enable_sozip: Optional[str]=None
           Whether to automatically/systematically/never apply the SOZIP optimization
       sozip_chunk_size: Optional[str]=None
           Chunk size for a seek-optimized file
       sozip_min_file_size: Optional[str]=None
           Minimum file size to decide if a file should be seek-optimized
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------
       output_string: str
           Output string, in which the result is placed


    """
    ...


def validate(input: str | os.PathLike[str], progress: Callable[[float, str, object], bool] | None = None, **kwargs) -> str:
    """Validate a ZIP file, possibly using SOZIP optimization.

       Consult https://gdal.org/programs/gdal_vsi_sozip.html for more details.

       Parameters
       ----------
       input: Union[str, os.PathLike[str]]
           Input ZIP filename
       progress: Optional[Callable[[float, str, object], bool]]=None
           Progress callback


       Output parameters
       -----------------
       output_string: str
           Output string, in which the result is placed


    """
    ...


