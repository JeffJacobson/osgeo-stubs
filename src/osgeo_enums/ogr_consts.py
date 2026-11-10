import enum
from typing import Literal

type ALTER = Literal[
    1, 2, 4, 8, 8, 16, 32, 64, 128, 256, 511, 4096, 8192, 16384, 32768, 65536, 126976
]


class ALTEREnum(enum.IntEnum):
    ALTER_NAME_FLAG = 1
    ALTER_TYPE_FLAG = 2
    ALTER_WIDTH_PRECISION_FLAG = 4
    ALTER_NULLABLE_FLAG = 8
    ALTER__FLAG = 8
    ALTER_DEFAULT_FLAG = 16
    ALTER_UNIQUE_FLAG = 32
    ALTER_DOMAIN_FLAG = 64
    ALTER_ALTERNATIVE_NAME_FLAG = 128
    ALTER_COMMENT_FLAG = 256
    ALTER_ALL_FLAG = 511
    ALTER_GEOM_FIELD_DEFN_NAME_FLAG = 4096
    ALTER_GEOM_FIELD_DEFN_TYPE_FLAG = 8192
    ALTER_GEOM_FIELD_DEFN_NULLABLE_FLAG = 16384
    ALTER_GEOM_FIELD_DEFN_SRS_FLAG = 32768
    ALTER_GEOM_FIELD_DEFN_SRS_COORD_EPOCH_FLAG = 65536
    ALTER_GEOM_FIELD_DEFN_ALL_FLAG = 126976


type F_VAL = Literal[-1, 1, 2, 4, 8]


class F_VALEnum(enum.IntEnum):
    F_VAL_ALL = -1
    F_VAL_NULL = 1
    F_VAL_GEOM_TYPE = 2
    F_VAL_WIDTH = 4
    F_VAL_ALLOW_NULL_WHEN_DEFAULT = 8


type GEOS_PREC = Literal[1, 2]


class GEOS_PRECEnum(enum.IntEnum):
    GEOS_PREC_NO_TOPO = 1
    GEOS_PREC_KEEP_COLLAPSED = 2


type GGT = Literal[1, 2, 4]


class GGTEnum(enum.IntEnum):
    GGT_COUNT_NOT_NEEDED = 1
    GGT_STOP_IF_MIXED = 2
    GGT_GEOMCOLLECTIONZ_TINZ = 4


type ODrC = Literal["CreateDataSource", "DeleteDataSource"]


class ODrCEnum(enum.StrEnum):
    ODrCCreateDataSource = "CreateDataSource"
    ODrCDeleteDataSource = "DeleteDataSource"


type ODsC = Literal[
    "AddFieldDomain",
    "AddRelationship",
    "CreateGeomFieldAfterCreateLayer",
    "CreateLayer",
    "CurveGeometries",
    "DeleteFieldDomain",
    "DeleteLayer",
    "DeleteRelationship",
    "EmulatedTransactions",
    "MeasuredGeometries",
    "RandomLayerRead",
    "RandomLayerWrite ",
    "Transactions",
    "UpdateFieldDomain",
    "UpdateRelationship",
    "ZGeometries",
]


class ODsCEnum(enum.StrEnum):
    ODsCAddFieldDomain = "AddFieldDomain"
    ODsCAddRelationship = "AddRelationship"
    ODsCCreateGeomFieldAfterCreateLayer = "CreateGeomFieldAfterCreateLayer"
    ODsCCreateLayer = "CreateLayer"
    ODsCCurveGeometries = "CurveGeometries"
    ODsCDeleteFieldDomain = "DeleteFieldDomain"
    ODsCDeleteLayer = "DeleteLayer"
    ODsCDeleteRelationship = "DeleteRelationship"
    ODsCEmulatedTransactions = "EmulatedTransactions"
    ODsCMeasuredGeometries = "MeasuredGeometries"
    ODsCRandomLayerRead = "RandomLayerRead"
    ODsCRandomLayerWrite = "RandomLayerWrite "
    ODsCTransactions = "Transactions"
    ODsCUpdateFieldDomain = "UpdateFieldDomain"
    ODsCUpdateRelationship = "UpdateRelationship"
    ODsCZGeometries = "ZGeometries"


type OFDMP = Literal[0, 1, 2]


class OFDMPEnum(enum.IntEnum):
    OFDMP_DEFAULT_VALUE = 0
    OFDMP_SUM = 1
    OFDMP_GEOMETRY_WEIGHTED = 2


type OFDSP = Literal[0, 1, 2]


class OFDSPEnum(enum.IntEnum):
    OFDSP_DEFAULT_VALUE = 0
    OFDSP_DUPLICATE = 1
    OFDSP_GEOMETRY_RATIO = 2


type OFDT = Literal[0, 1, 2]


class OFDTEnum(enum.IntEnum):
    OFDT_CODED = 0
    OFDT_RANGE = 1
    OFDT_GLOB = 2


type OGRERR = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


class OGRERREnum(enum.IntEnum):
    OGRERR_NONE = 0
    OGRERR_NOT_ENOUGH_DATA = 1
    OGRERR_NOT_ENOUGH_MEMORY = 2
    OGRERR_UNSUPPORTED_GEOMETRY_TYPE = 3
    OGRERR_UNSUPPORTED_OPERATION = 4
    OGRERR_CORRUPT_DATA = 5
    OGRERR_FAILURE = 6
    OGRERR_UNSUPPORTED_SRS = 7
    OGRERR_INVALID_HANDLE = 8
    OGRERR_NON_EXISTING_FEATURE = 9


type OLMD = Literal["OLMD_FID64"]


class OLMDEnum(enum.StrEnum):
    OLMD_FID64 = "OLMD_FID64"


type TZFLAG = Literal[0, 1, 2, 100]


class TZFLAGEnum(enum.IntEnum):
    TZFLAG_UNKNOWN = 0
    TZFLAG_LOCALTIME = 1
    TZFLAG_MIXED_TZ = 2
    TZFLAG_UTC = 100


type wkb = Literal[
    -2147483648,
    -2147483648,
    -2147483647,
    -2147483646,
    -2147483645,
    -2147483644,
    -2147483643,
    -2147483642,
    -2147483641,
    0,
    0,
    1,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    100,
    101,
    1008,
    1009,
    1010,
    1011,
    1012,
    1013,
    1014,
    1015,
    1016,
    1017,
    2001,
    2002,
    2003,
    2004,
    2005,
    2006,
    2007,
    2008,
    2009,
    2010,
    2011,
    2012,
    2013,
    2014,
    2015,
    2016,
    2017,
    3001,
    3002,
    3003,
    3004,
    3005,
    3006,
    3007,
    3008,
    3009,
    3010,
    3011,
    3012,
    3013,
    3014,
    3015,
    3016,
    3017,
]


class wkbEnum(enum.IntEnum):
    wkb25Bit = -2147483648
    wkb25DBit = -2147483648
    wkbPoint25D = -2147483647
    wkbLineString25D = -2147483646
    wkbPolygon25D = -2147483645
    wkbMultiPoint25D = -2147483644
    wkbMultiLineString25D = -2147483643
    wkbMultiPolygon25D = -2147483642
    wkbGeometryCollection25D = -2147483641
    wkbUnknown = 0
    wkbXDR = 0
    wkbNDR = 1
    wkbPoint = 1
    wkbLineString = 2
    wkbPolygon = 3
    wkbMultiPoint = 4
    wkbMultiLineString = 5
    wkbMultiPolygon = 6
    wkbGeometryCollection = 7
    wkbCircularString = 8
    wkbCompoundCurve = 9
    wkbCurvePolygon = 10
    wkbMultiCurve = 11
    wkbMultiSurface = 12
    wkbCurve = 13
    wkbSurface = 14
    wkbPolyhedralSurface = 15
    wkbTIN = 16
    wkbTriangle = 17
    wkbNone = 100
    wkbLinearRing = 101
    wkbCircularStringZ = 1008
    wkbCompoundCurveZ = 1009
    wkbCurvePolygonZ = 1010
    wkbMultiCurveZ = 1011
    wkbMultiSurfaceZ = 1012
    wkbCurveZ = 1013
    wkbSurfaceZ = 1014
    wkbPolyhedralSurfaceZ = 1015
    wkbTINZ = 1016
    wkbTriangleZ = 1017
    wkbPointM = 2001
    wkbLineStringM = 2002
    wkbPolygonM = 2003
    wkbMultiPointM = 2004
    wkbMultiLineStringM = 2005
    wkbMultiPolygonM = 2006
    wkbGeometryCollectionM = 2007
    wkbCircularStringM = 2008
    wkbCompoundCurveM = 2009
    wkbCurvePolygonM = 2010
    wkbMultiCurveM = 2011
    wkbMultiSurfaceM = 2012
    wkbCurveM = 2013
    wkbSurfaceM = 2014
    wkbPolyhedralSurfaceM = 2015
    wkbTINM = 2016
    wkbTriangleM = 2017
    wkbPointZM = 3001
    wkbLineStringZM = 3002
    wkbPolygonZM = 3003
    wkbMultiPointZM = 3004
    wkbMultiLineStringZM = 3005
    wkbMultiPolygonZM = 3006
    wkbGeometryCollectionZM = 3007
    wkbCircularStringZM = 3008
    wkbCompoundCurveZM = 3009
    wkbCurvePolygonZM = 3010
    wkbMultiCurveZM = 3011
    wkbMultiSurfaceZM = 3012
    wkbCurveZM = 3013
    wkbSurfaceZM = 3014
    wkbPolyhedralSurfaceZM = 3015
    wkbTINZM = 3016
    wkbTriangleZM = 3017
