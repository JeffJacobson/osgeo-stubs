import enum
from typing import Literal

type OAMS = Literal[0, 1, 2]


class OAMSEnum(enum.IntEnum):
    OAMS_TRADITIONAL_GIS_ORDER = 0
    OAMS_AUTHORITY_COMPLIANT = 1
    OAMS_CUSTOM = 2


type OAO = Literal[0, 1, 2, 3, 4, 5, 6]


class OAOEnum(enum.IntEnum):
    OAO_Other = 0
    OAO_North = 1
    OAO_South = 2
    OAO_East = 3
    OAO_West = 4
    OAO_Up = 5
    OAO_Down = 6


type OSR_CRS_TYPE = Literal[0, 1, 2, 3, 4, 5, 6]


class OSR_CRS_TYPEEnum(enum.IntEnum):
    OSR_CRS_TYPE_GEOGRAPHIC_2D = 0
    OSR_CRS_TYPE_GEOGRAPHIC_3D = 1
    OSR_CRS_TYPE_GEOCENTRIC = 2
    OSR_CRS_TYPE_PROJECTED = 3
    OSR_CRS_TYPE_VERTICAL = 4
    OSR_CRS_TYPE_COMPOUND = 5
    OSR_CRS_TYPE_OTHER = 6


type PROJ_ERR = Literal[
    1024,
    1025,
    1026,
    1027,
    1028,
    1029,
    2048,
    2049,
    2050,
    2051,
    2052,
    2053,
    4096,
    4097,
    4098,
    4099,
]


class PROJ_ERREnum(enum.IntEnum):
    PROJ_ERR_INVALID_OP = 1024
    PROJ_ERR_INVALID_OP_WRONG_SYNTAX = 1025
    PROJ_ERR_INVALID_OP_MISSING_ARG = 1026
    PROJ_ERR_INVALID_OP_ILLEGAL_ARG_VALUE = 1027
    PROJ_ERR_INVALID_OP_MUTUALLY_EXCLUSIVE_ARGS = 1028
    PROJ_ERR_INVALID_OP_FILE_NOT_FOUND_OR_INVALID = 1029
    PROJ_ERR_COORD_TRANSFM = 2048
    PROJ_ERR_COORD_TRANSFM_INVALID_COORD = 2049
    PROJ_ERR_COORD_TRANSFM_OUTSIDE_PROJECTION_DOMAIN = 2050
    PROJ_ERR_COORD_TRANSFM_NO_OPERATION = 2051
    PROJ_ERR_COORD_TRANSFM_OUTSIDE_GRID = 2052
    PROJ_ERR_COORD_TRANSFM_GRID_AT_NODATA = 2053
    PROJ_ERR_OTHER = 4096
    PROJ_ERR_OTHER_API_MISUSE = 4097
    PROJ_ERR_OTHER_NO_INVERSE_OP = 4098
    PROJ_ERR_OTHER_NETWORK_ERROR = 4099


type SRS_DN = Literal[
    "North_American_Datum_1927", "North_American_Datum_1983", "WGS_1972", "WGS_1984"
]


class SRS_DNEnum(enum.StrEnum):
    SRS_DN_NAD27 = "North_American_Datum_1927"
    SRS_DN_NAD83 = "North_American_Datum_1983"
    SRS_DN_WGS72 = "WGS_1972"
    SRS_DN_WGS84 = "WGS_1984"


type SRS = Literal["Greenwich"]


class SRSEnum(enum.StrEnum):
    SRS_PM_GREENWICH = "Greenwich"


type SRS_PP = Literal[
    "Latitude_Of_1st_Point",
    "Latitude_Of_2nd_Point",
    "Longitude_Of_1st_Point",
    "Longitude_Of_2nd_Point",
    "azimuth",
    "central_meridian",
    "false_easting",
    "false_northing",
    "fipszone",
    "landsat_number",
    "latitude_of_center",
    "latitude_of_origin",
    "latitude_of_point_1",
    "latitude_of_point_2",
    "latitude_of_point_3",
    "longitude_of_center",
    "longitude_of_origin",
    "longitude_of_point_1",
    "longitude_of_point_2",
    "longitude_of_point_3",
    "path_number",
    "peg_point_heading",
    "peg_point_height",
    "peg_point_latitude",
    "peg_point_longitude",
    "perspective_point_height",
    "pseudo_standard_parallel_1",
    "rectified_grid_angle",
    "satellite_height",
    "scale_factor",
    "standard_parallel_1",
    "standard_parallel_2",
    "zone",
]


class SRS_PPEnum(enum.StrEnum):
    SRS_PP_LATITUDE_OF_1ST_POINT = "Latitude_Of_1st_Point"
    SRS_PP_LATITUDE_OF_2ND_POINT = "Latitude_Of_2nd_Point"
    SRS_PP_LONGITUDE_OF_1ST_POINT = "Longitude_Of_1st_Point"
    SRS_PP_LONGITUDE_OF_2ND_POINT = "Longitude_Of_2nd_Point"
    SRS_PP_AZIMUTH = "azimuth"
    SRS_PP_CENTRAL_MERIDIAN = "central_meridian"
    SRS_PP_FALSE_EASTING = "false_easting"
    SRS_PP_FALSE_NORTHING = "false_northing"
    SRS_PP_FIPSZONE = "fipszone"
    SRS_PP_LANDSAT_NUMBER = "landsat_number"
    SRS_PP_LATITUDE_OF_CENTER = "latitude_of_center"
    SRS_PP_LATITUDE_OF_ORIGIN = "latitude_of_origin"
    SRS_PP_LATITUDE_OF_POINT_1 = "latitude_of_point_1"
    SRS_PP_LATITUDE_OF_POINT_2 = "latitude_of_point_2"
    SRS_PP_LATITUDE_OF_POINT_3 = "latitude_of_point_3"
    SRS_PP_LONGITUDE_OF_CENTER = "longitude_of_center"
    SRS_PP_LONGITUDE_OF_ORIGIN = "longitude_of_origin"
    SRS_PP_LONGITUDE_OF_POINT_1 = "longitude_of_point_1"
    SRS_PP_LONGITUDE_OF_POINT_2 = "longitude_of_point_2"
    SRS_PP_LONGITUDE_OF_POINT_3 = "longitude_of_point_3"
    SRS_PP_PATH_NUMBER = "path_number"
    SRS_PP_PEG_POINT_HEADING = "peg_point_heading"
    SRS_PP_PEG_POINT_HEIGHT = "peg_point_height"
    SRS_PP_PEG_POINT_LATITUDE = "peg_point_latitude"
    SRS_PP_PEG_POINT_LONGITUDE = "peg_point_longitude"
    SRS_PP_PERSPECTIVE_POINT_HEIGHT = "perspective_point_height"
    SRS_PP_PSEUDO_STD_PARALLEL_1 = "pseudo_standard_parallel_1"
    SRS_PP_RECTIFIED_GRID_ANGLE = "rectified_grid_angle"
    SRS_PP_SATELLITE_HEIGHT = "satellite_height"
    SRS_PP_SCALE_FACTOR = "scale_factor"
    SRS_PP_STANDARD_PARALLEL_1 = "standard_parallel_1"
    SRS_PP_STANDARD_PARALLEL_2 = "standard_parallel_2"
    SRS_PP_ZONE = "zone"


type SRS_PT = Literal[
    "Aitoff",
    "Albers_Conic_Equal_Area",
    "Azimuthal_Equidistant",
    "Bonne",
    "Cassini_Soldner",
    "Craster_Parabolic",
    "Cylindrical_Equal_Area",
    "Eckert_I",
    "Eckert_II",
    "Eckert_III",
    "Eckert_IV",
    "Eckert_V",
    "Eckert_VI",
    "Equidistant_Conic",
    "Equirectangular",
    "Gall_Stereographic",
    "Gauss_Schreiber_Transverse_Mercator",
    "Geostationary_Satellite",
    "Gnomonic",
    "Goode_Homolosine",
    "Hotine_Oblique_Mercator",
    "Hotine_Oblique_Mercator_Azimuth_Center",
    "Hotine_Oblique_Mercator_Two_Point_Natural_Origin",
    "International_Map_of_the_World_Polyconic",
    "Interrupted_Goode_Homolosine",
    "Krovak",
    "Laborde_Oblique_Mercator",
    "Lambert_Azimuthal_Equal_Area",
    "Lambert_Conformal_Conic_1SP",
    "Lambert_Conformal_Conic_2SP",
    "Lambert_Conformal_Conic_2SP_Belgium",
    "Loximuthal",
    "Mercator_1SP",
    "Mercator_2SP",
    "Mercator_Auxiliary_Sphere",
    "Miller_Cylindrical",
    "Mollweide",
    "New_Zealand_Map_Grid",
    "Oblique_Stereographic",
    "Orthographic",
    "Polar_Stereographic",
    "Polyconic",
    "Quadrilateralized_Spherical_Cube",
    "Quartic_Authalic",
    "Robinson",
    "Sinusoidal",
    "Spherical_Cross_Track_Height",
    "Stereographic",
    "Swiss_Oblique_Cylindrical",
    "Transverse_Mercator",
    "Transverse_Mercator_MapInfo_21",
    "Transverse_Mercator_MapInfo_22",
    "Transverse_Mercator_MapInfo_23",
    "Transverse_Mercator_MapInfo_24",
    "Transverse_Mercator_MapInfo_25",
    "Transverse_Mercator_South_Orientated",
    "Tunisia_Mining_Grid",
    "Two_Point_Equidistant",
    "VanDerGrinten",
    "Wagner_I",
    "Wagner_II",
    "Wagner_III",
    "Wagner_IV",
    "Wagner_V",
    "Wagner_VI",
    "Wagner_VII",
    "Winkel_I",
    "Winkel_II",
    "Winkel_Tripel",
]


class SRS_PTEnum(enum.StrEnum):
    SRS_PT_AITOFF = "Aitoff"
    SRS_PT_ALBERS_CONIC_EQUAL_AREA = "Albers_Conic_Equal_Area"
    SRS_PT_AZIMUTHAL_EQUIDISTANT = "Azimuthal_Equidistant"
    SRS_PT_BONNE = "Bonne"
    SRS_PT_CASSINI_SOLDNER = "Cassini_Soldner"
    SRS_PT_CRASTER_PARABOLIC = "Craster_Parabolic"
    SRS_PT_CYLINDRICAL_EQUAL_AREA = "Cylindrical_Equal_Area"
    SRS_PT_ECKERT_I = "Eckert_I"
    SRS_PT_ECKERT_II = "Eckert_II"
    SRS_PT_ECKERT_III = "Eckert_III"
    SRS_PT_ECKERT_IV = "Eckert_IV"
    SRS_PT_ECKERT_V = "Eckert_V"
    SRS_PT_ECKERT_VI = "Eckert_VI"
    SRS_PT_EQUIDISTANT_CONIC = "Equidistant_Conic"
    SRS_PT_EQUIRECTANGULAR = "Equirectangular"
    SRS_PT_GALL_STEREOGRAPHIC = "Gall_Stereographic"
    SRS_PT_GAUSSSCHREIBERTMERCATOR = "Gauss_Schreiber_Transverse_Mercator"
    SRS_PT_GEOSTATIONARY_SATELLITE = "Geostationary_Satellite"
    SRS_PT_GNOMONIC = "Gnomonic"
    SRS_PT_GOODE_HOMOLOSINE = "Goode_Homolosine"
    SRS_PT_HOTINE_OBLIQUE_MERCATOR = "Hotine_Oblique_Mercator"
    SRS_PT_HOTINE_OBLIQUE_MERCATOR_AZIMUTH_CENTER = (
        "Hotine_Oblique_Mercator_Azimuth_Center"
    )
    SRS_PT_HOTINE_OBLIQUE_MERCATOR_TWO_POINT_NATURAL_ORIGIN = (
        "Hotine_Oblique_Mercator_Two_Point_Natural_Origin"
    )
    SRS_PT_IMW_POLYCONIC = "International_Map_of_the_World_Polyconic"
    SRS_PT_IGH = "Interrupted_Goode_Homolosine"
    SRS_PT_KROVAK = "Krovak"
    SRS_PT_LABORDE_OBLIQUE_MERCATOR = "Laborde_Oblique_Mercator"
    SRS_PT_LAMBERT_AZIMUTHAL_EQUAL_AREA = "Lambert_Azimuthal_Equal_Area"
    SRS_PT_LAMBERT_CONFORMAL_CONIC_1SP = "Lambert_Conformal_Conic_1SP"
    SRS_PT_LAMBERT_CONFORMAL_CONIC_2SP = "Lambert_Conformal_Conic_2SP"
    SRS_PT_LAMBERT_CONFORMAL_CONIC_2SP_BELGIUM = "Lambert_Conformal_Conic_2SP_Belgium"
    SRS_PT_LOXIMUTHAL = "Loximuthal"
    SRS_PT_MERCATOR_1SP = "Mercator_1SP"
    SRS_PT_MERCATOR_2SP = "Mercator_2SP"
    SRS_PT_MERCATOR_AUXILIARY_SPHERE = "Mercator_Auxiliary_Sphere"
    SRS_PT_MILLER_CYLINDRICAL = "Miller_Cylindrical"
    SRS_PT_MOLLWEIDE = "Mollweide"
    SRS_PT_NEW_ZEALAND_MAP_GRID = "New_Zealand_Map_Grid"
    SRS_PT_OBLIQUE_STEREOGRAPHIC = "Oblique_Stereographic"
    SRS_PT_ORTHOGRAPHIC = "Orthographic"
    SRS_PT_POLAR_STEREOGRAPHIC = "Polar_Stereographic"
    SRS_PT_POLYCONIC = "Polyconic"
    SRS_PT_QSC = "Quadrilateralized_Spherical_Cube"
    SRS_PT_QUARTIC_AUTHALIC = "Quartic_Authalic"
    SRS_PT_ROBINSON = "Robinson"
    SRS_PT_SINUSOIDAL = "Sinusoidal"
    SRS_PT_SCH = "Spherical_Cross_Track_Height"
    SRS_PT_STEREOGRAPHIC = "Stereographic"
    SRS_PT_SWISS_OBLIQUE_CYLINDRICAL = "Swiss_Oblique_Cylindrical"
    SRS_PT_TRANSVERSE_MERCATOR = "Transverse_Mercator"
    SRS_PT_TRANSVERSE_MERCATOR_MI_21 = "Transverse_Mercator_MapInfo_21"
    SRS_PT_TRANSVERSE_MERCATOR_MI_22 = "Transverse_Mercator_MapInfo_22"
    SRS_PT_TRANSVERSE_MERCATOR_MI_23 = "Transverse_Mercator_MapInfo_23"
    SRS_PT_TRANSVERSE_MERCATOR_MI_24 = "Transverse_Mercator_MapInfo_24"
    SRS_PT_TRANSVERSE_MERCATOR_MI_25 = "Transverse_Mercator_MapInfo_25"
    SRS_PT_TRANSVERSE_MERCATOR_SOUTH_ORIENTED = "Transverse_Mercator_South_Orientated"
    SRS_PT_TUNISIA_MINING_GRID = "Tunisia_Mining_Grid"
    SRS_PT_TWO_POINT_EQUIDISTANT = "Two_Point_Equidistant"
    SRS_PT_VANDERGRINTEN = "VanDerGrinten"
    SRS_PT_WAGNER_I = "Wagner_I"
    SRS_PT_WAGNER_II = "Wagner_II"
    SRS_PT_WAGNER_III = "Wagner_III"
    SRS_PT_WAGNER_IV = "Wagner_IV"
    SRS_PT_WAGNER_V = "Wagner_V"
    SRS_PT_WAGNER_VI = "Wagner_VI"
    SRS_PT_WAGNER_VII = "Wagner_VII"
    SRS_PT_WINKEL_I = "Winkel_I"
    SRS_PT_WINKEL_II = "Winkel_II"
    SRS_PT_WINKEL_TRIPEL = "Winkel_Tripel"


type SRS_UA = Literal["0.0174532925199433", "degree", "radian"]


class SRS_UAEnum(enum.StrEnum):
    SRS_UA_DEGREE_CONV = "0.0174532925199433"
    SRS_UA_DEGREE = "degree"
    SRS_UA_RADIAN = "radian"


type SRS_UL = Literal[
    "0.001",
    "0.01",
    "0.0254",
    "0.025400050800101603",
    "0.1",
    "0.2011661949",
    "0.20116684023368047",
    "0.201168",
    "0.30479841",
    "0.3048",
    "0.3048",
    "0.3048006096012192",
    "0.91439523",
    "0.9144",
    "0.914401828803658",
    "1.8288",
    "1000.",
    "1609.344",
    "1609.347218694437",
    "1852.0",
    "1852.0",
    "20.116684023368047",
    "20.11669506",
    "20.1168",
    "20.11684023368047",
    "5.02921005842012",
    "Centimeter",
    "Chain",
    "Chain_Indian",
    "Chain_International",
    "Chain_US_Surveyor",
    "Decimeter",
    "Fathom_International",
    "Foot (International)",
    "Foot_Indian",
    "Foot_International",
    "Foot_US",
    "Inch_International",
    "Inch_US_Surveyor",
    "Kilometer",
    "Link",
    "Link_Clarke",
    "Link_International",
    "Meter",
    "Millimeter",
    "Nautical Mile",
    "Nautical_Mile_International",
    "Rod",
    "Statute_Mile_International",
    "Statute_Mile_US_Surveyor",
    "Yard_Indian",
    "Yard_International",
    "Yard_US_Surveyor",
]


class SRS_ULEnum(enum.StrEnum):
    SRS_UL_MILLIMETER_CONV = "0.001"
    SRS_UL_CENTIMETER_CONV = "0.01"
    SRS_UL_INTL_INCH_CONV = "0.0254"
    SRS_UL_US_INCH_CONV = "0.025400050800101603"
    SRS_UL_DECIMETER_CONV = "0.1"
    SRS_UL_LINK_Clarke_CONV = "0.2011661949"
    SRS_UL_LINK_CONV = "0.20116684023368047"
    SRS_UL_INTL_LINK_CONV = "0.201168"
    SRS_UL_INDIAN_FOOT_CONV = "0.30479841"
    SRS_UL_FOOT_CONV = "0.3048"
    SRS_UL_INTL_FOOT_CONV = "0.3048"
    SRS_UL_US_FOOT_CONV = "0.3048006096012192"
    SRS_UL_INDIAN_YARD_CONV = "0.91439523"
    SRS_UL_INTL_YARD_CONV = "0.9144"
    SRS_UL_US_YARD_CONV = "0.914401828803658"
    SRS_UL_INTL_FATHOM_CONV = "1.8288"
    SRS_UL_KILOMETER_CONV = "1000."
    SRS_UL_INTL_STAT_MILE_CONV = "1609.344"
    SRS_UL_US_STAT_MILE_CONV = "1609.347218694437"
    SRS_UL_INTL_NAUT_MILE_CONV = "1852.0"
    SRS_UL_NAUTICAL_MILE_CONV = "1852.0"
    SRS_UL_CHAIN_CONV = "20.116684023368047"
    SRS_UL_INDIAN_CHAIN_CONV = "20.11669506"
    SRS_UL_INTL_CHAIN_CONV = "20.1168"
    SRS_UL_US_CHAIN_CONV = "20.11684023368047"
    SRS_UL_ROD_CONV = "5.02921005842012"
    SRS_UL_CENTIMETER = "Centimeter"
    SRS_UL_CHAIN = "Chain"
    SRS_UL_INDIAN_CHAIN = "Chain_Indian"
    SRS_UL_INTL_CHAIN = "Chain_International"
    SRS_UL_US_CHAIN = "Chain_US_Surveyor"
    SRS_UL_DECIMETER = "Decimeter"
    SRS_UL_INTL_FATHOM = "Fathom_International"
    SRS_UL_FOOT = "Foot (International)"
    SRS_UL_INDIAN_FOOT = "Foot_Indian"
    SRS_UL_INTL_FOOT = "Foot_International"
    SRS_UL_US_FOOT = "Foot_US"
    SRS_UL_INTL_INCH = "Inch_International"
    SRS_UL_US_INCH = "Inch_US_Surveyor"
    SRS_UL_KILOMETER = "Kilometer"
    SRS_UL_LINK = "Link"
    SRS_UL_LINK_Clarke = "Link_Clarke"
    SRS_UL_INTL_LINK = "Link_International"
    SRS_UL_METER = "Meter"
    SRS_UL_MILLIMETER = "Millimeter"
    SRS_UL_NAUTICAL_MILE = "Nautical Mile"
    SRS_UL_INTL_NAUT_MILE = "Nautical_Mile_International"
    SRS_UL_ROD = "Rod"
    SRS_UL_INTL_STAT_MILE = "Statute_Mile_International"
    SRS_UL_US_STAT_MILE = "Statute_Mile_US_Surveyor"
    SRS_UL_INDIAN_YARD = "Yard_Indian"
    SRS_UL_INTL_YARD = "Yard_International"
    SRS_UL_US_YARD = "Yard_US_Surveyor"


type SRS_WGS84 = Literal[298.257223563, 6378137.0]


class SRS_WGS84Enum(enum.Enum):
    SRS_WGS84_INVFLATTENING = 298.257223563
    SRS_WGS84_SEMIMAJOR = 6378137.0


type SRS_WKT = Literal[
    (
        'GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS '
        '84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AXIS["Latitude",NORTH],AXIS["Longitude",EAST],AUTHORITY["EPSG","4326"]]'
    )
]


class SRS_WKTEnum(enum.StrEnum):
    SRS_WKT_WGS84_LAT_LONG = (
        'GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS '
        '84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AXIS["Latitude",NORTH],AXIS["Longitude",EAST],AUTHORITY["EPSG","4326"]]'
    )
