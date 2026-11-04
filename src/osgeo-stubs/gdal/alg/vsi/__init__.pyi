from collections.abc import Callable

from osgeo import gdal

def copy(
    source: str,
    destination: str,
    recursive: bool | None = None,
    skip_errors: bool | None = None,
    quiet: bool | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Copy files located on GDAL Virtual System Interface (VSI).

    Consult https://gdal.org/programs/gdal_vsi_copy.html for more details.

    Parameters
    ----------
    source: str
        Source file or directory name
    destination: str
        Destination file or directory name
    recursive: Optional[bool]=None
        Copy subdirectories recursively
    skip_errors: Optional[bool]=None
        Skip errors
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------


    """
    ...

def delete(
    filename: str,
    recursive: bool | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Delete files located on GDAL Virtual System Interface (VSI).

    Consult https://gdal.org/programs/gdal_vsi_delete.html for more details.

    Parameters
    ----------
    filename: str
        File or directory name to delete
    recursive: Optional[bool]=None
        Delete directories recursively
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------


    """
    ...

def list(
    filename: str,
    output_format: str | None = None,
    long_listing: bool | None = None,
    recursive: bool | None = None,
    depth: int | None = None,
    absolute_path: bool | None = None,
    tree: bool | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """List files of one of the GDAL Virtual System Interface (VSI).

    Consult https://gdal.org/programs/gdal_vsi_list.html for more details.

    Parameters
    ----------
    filename: str
        File or directory name
    output_format: Optional[str]=None
        Aliases: format
        Output format
    long_listing: Optional[bool]=None
        Aliases: long
        Use a long listing format
    recursive: Optional[bool]=None
        List subdirectories recursively
    depth: Optional[int]=None
        Maximum depth in recursive mode
    absolute_path: Optional[bool]=None
        Display absolute path
    tree: Optional[bool]=None
        Use a hierarchical presentation for JSON output
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------
    output_string: str
        Output string, in which the result is placed


    """
    ...

def move(
    source: str,
    destination: str,
    quiet: bool | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
    """Move/rename a file/directory located on GDAL Virtual System Interface (VSI).

    Consult https://gdal.org/programs/gdal_vsi_move.html for more details.

    Parameters
    ----------
    source: str
        Source file or directory name
    destination: str
        Destination file or directory name
    quiet: Optional[bool]=None
        Quiet mode (no progress bar or warning message)
    progress: Optional[Callable[[float, str, object], bool]]=None
        Progress callback


    Output parameters
    -----------------


    """
    ...

def sync(
    source: str,
    destination: str,
    quiet: bool | None = None,
    recursive: bool | None = None,
    strategy: str | None = None,
    num_threads: str | None = None,
    progress: Callable[[float, str, object], bool] | None = None,
    **kwargs,
) -> gdal.Algorithm:
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
