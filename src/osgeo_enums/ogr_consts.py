import enum


class ALTEREnum(enum.Enum):
    ALTER_NAME_FLAG = 1
    ALTER_GEOM_FIELD_DEFN_ALL_FLAG = 126976
    ALTER_ALTERNATIVE_NAME_FLAG = 128
    ALTER_DEFAULT_FLAG = 16
    ALTER_GEOM_FIELD_DEFN_NULLABLE_FLAG = 16384
    ALTER_TYPE_FLAG = 2
    ALTER_COMMENT_FLAG = 256
    ALTER_UNIQUE_FLAG = 32
    ALTER_GEOM_FIELD_DEFN_SRS_FLAG = 32768
    ALTER_WIDTH_PRECISION_FLAG = 4
    ALTER_GEOM_FIELD_DEFN_NAME_FLAG = 4096
    ALTER_ALL_FLAG = 511
    ALTER_DOMAIN_FLAG = 64
    ALTER_GEOM_FIELD_DEFN_SRS_COORD_EPOCH_FLAG = 65536
    ALTER_NULLABLE_FLAG = 8
    ALTER__FLAG = 8
    ALTER_GEOM_FIELD_DEFN_TYPE_FLAG = 8192 


class F_VALEnum(enum.Enum):
    F_VAL_ALL = -1
    F_VAL_NULL = 1
    F_VAL_GEOM_TYPE = 2
    F_VAL_WIDTH = 4
    F_VAL_ALLOW_NULL_WHEN_DEFAULT = 8 


class GEOS_PRECEnum(enum.Enum):
    GEOS_PREC_NO_TOPO = 1
    GEOS_PREC_KEEP_COLLAPSED = 2 


class GGTEnum(enum.Enum):
    GGT_COUNT_NOT_NEEDED = 1
    GGT_STOP_IF_MIXED = 2
    GGT_GEOMCOLLECTIONZ_TINZ = 4 


class ODrCEnum(enum.Enum):
    ODrCCreateDataSource = 'CreateDataSource'
    ODrCDeleteDataSource = 'DeleteDataSource' 


class ODsCEnum(enum.Enum):
    ODsCAddFieldDomain = 'AddFieldDomain'
    ODsCAddRelationship = 'AddRelationship'
    ODsCCreateGeomFieldAfterCreateLayer = 'CreateGeomFieldAfterCreateLayer'
    ODsCCreateLayer = 'CreateLayer'
    ODsCCurveGeometries = 'CurveGeometries'
    ODsCDeleteFieldDomain = 'DeleteFieldDomain'
    ODsCDeleteLayer = 'DeleteLayer'
    ODsCDeleteRelationship = 'DeleteRelationship'
    ODsCEmulatedTransactions = 'EmulatedTransactions'
    ODsCMeasuredGeometries = 'MeasuredGeometries'
    ODsCRandomLayerRead = 'RandomLayerRead'
    ODsCRandomLayerWrite = 'RandomLayerWrite '
    ODsCTransactions = 'Transactions'
    ODsCUpdateFieldDomain = 'UpdateFieldDomain'
    ODsCUpdateRelationship = 'UpdateRelationship'
    ODsCZGeometries = 'ZGeometries' 


class OFDMPEnum(enum.Enum):
    OFDMP_DEFAULT_VALUE = 0
    OFDMP_SUM = 1
    OFDMP_GEOMETRY_WEIGHTED = 2 


class OFDSPEnum(enum.Enum):
    OFDSP_DEFAULT_VALUE = 0
    OFDSP_DUPLICATE = 1
    OFDSP_GEOMETRY_RATIO = 2 


class OFDTEnum(enum.Enum):
    OFDT_CODED = 0
    OFDT_RANGE = 1
    OFDT_GLOB = 2 


class OGRERREnum(enum.Enum):
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


class OLMDEnum(enum.Enum):
    OLMD_FID64 = 'OLMD_FID64' 


class TZFLAGEnum(enum.Enum):
    TZFLAG_UNKNOWN = 0
    TZFLAG_LOCALTIME = 1
    TZFLAG_UTC = 100
    TZFLAG_MIXED_TZ = 2 


class wkbEnum(enum.Enum):
    wkbGeometryCollection25D = -2147483641
    wkbMultiPolygon25D = -2147483642
    wkbMultiLineString25D = -2147483643
    wkbMultiPoint25D = -2147483644
    wkbPolygon25D = -2147483645
    wkbLineString25D = -2147483646
    wkbPoint25D = -2147483647
    wkb25Bit = -2147483648
    wkb25DBit = -2147483648
    wkbUnknown = 0
    wkbXDR = 0
    wkbNDR = 1
    wkbPoint = 1
    wkbCurvePolygon = 10
    wkbNone = 100
    wkbCircularStringZ = 1008
    wkbCompoundCurveZ = 1009
    wkbLinearRing = 101
    wkbCurvePolygonZ = 1010
    wkbMultiCurveZ = 1011
    wkbMultiSurfaceZ = 1012
    wkbCurveZ = 1013
    wkbSurfaceZ = 1014
    wkbPolyhedralSurfaceZ = 1015
    wkbTINZ = 1016
    wkbTriangleZ = 1017
    wkbMultiCurve = 11
    wkbMultiSurface = 12
    wkbCurve = 13
    wkbSurface = 14
    wkbPolyhedralSurface = 15
    wkbTIN = 16
    wkbTriangle = 17
    wkbLineString = 2
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
    wkbPolygon = 3
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
    wkbMultiPoint = 4
    wkbMultiLineString = 5
    wkbMultiPolygon = 6
    wkbGeometryCollection = 7
    wkbCircularString = 8
    wkbCompoundCurve = 9 


