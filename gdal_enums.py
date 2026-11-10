import enum


class CE(enum.Enum):
    CE_None = 0
    CE_Debug = 1
    CE_Warning = 2
    CE_Failure = 3
    CE_Fatal = 4


class CPLES(enum.Enum):
    CPLES_BackslashQuotable = 0
    CPLES_XML = 1
    CPLES_URL = 2
    CPLES_SQL = 3
    CPLES_CSV = 4
    CPLES_XML_BUT_QUOTES = 5
    CPLES_SQLI = 7


class CPLE(enum.Enum):
    CPLE_None = 0
    CPLE_AppDefined = 1
    CPLE_ObjectNull = 10
    CPLE_HttpResponse = 11
    CPLE_AWSBucketNotFound = 12
    CPLE_AWSObjectNotFound = 13
    CPLE_AWSAccessDenied = 14
    CPLE_AWSInvalidCredentials = 15
    CPLE_AWSSignatureDoesNotMatch = 16
    CPLE_ObjectStorageGenericError = 17
    CPLE_OutOfMemory = 2
    CPLE_FileIO = 3
    CPLE_OpenFailed = 4
    CPLE_IllegalArg = 5
    CPLE_NotSupported = 6
    CPLE_AssertionFailed = 7
    CPLE_NoWriteAccess = 8
    CPLE_UserInterrupt = 9


class CXT(enum.Enum):
    CXT_Element = 0
    CXT_Text = 1
    CXT_Attribute = 2
    CXT_Comment = 3
    CXT_Literal = 4


class DCAP(enum.Enum):
    DCAP_APPEND = 'DCAP_APPEND'
    DCAP_COORDINATE_EPOCH = 'DCAP_COORDINATE_EPOCH'
    DCAP_CREATE = 'DCAP_CREATE'
    DCAP_CREATECOPY = 'DCAP_CREATECOPY'
    DCAP_CREATECOPY_MULTIDIMENSIONAL = 'DCAP_CREATECOPY_MULTIDIMENSIONAL'
    DCAP_CREATE_FIELD = 'DCAP_CREATE_FIELD'
    DCAP_CREATE_LAYER = 'DCAP_CREATE_LAYER'
    DCAP_CREATE_MULTIDIMENSIONAL = 'DCAP_CREATE_MULTIDIMENSIONAL'
    DCAP_CREATE_ONLY_VISIBLE_AT_CLOSE_TIME = 'DCAP_CREATE_ONLY_VISIBLE_AT_CLOSE_TIME'
    DCAP_CURVE_GEOMETRIES = 'DCAP_CURVE_GEOMETRIES'
    DCAP_DEFAULT_FIELDS = 'DCAP_DEFAULT_FIELDS'
    DCAP_DELETE_FIELD = 'DCAP_DELETE_FIELD'
    DCAP_DELETE_LAYER = 'DCAP_DELETE_LAYER'
    DCAP_FEATURE_STYLES = 'DCAP_FEATURE_STYLES'
    DCAP_FEATURE_STYLES_READ = 'DCAP_FEATURE_STYLES_READ'
    DCAP_FEATURE_STYLES_WRITE = 'DCAP_FEATURE_STYLES_WRITE'
    DCAP_FIELD_DOMAINS = 'DCAP_FIELD_DOMAINS'
    DCAP_FLUSHCACHE_CONSISTENT_STATE = 'DCAP_FLUSHCACHE_CONSISTENT_STATE'
    DCAP_GNM = 'DCAP_GNM'
    DCAP_MEASURED_GEOMETRIES = 'DCAP_MEASURED_GEOMETRIES'
    DCAP_MULTIDIM_RASTER = 'DCAP_MULTIDIM_RASTER'
    DCAP_MULTIPLE_VECTOR_LAYERS = 'DCAP_MULTIPLE_VECTOR_LAYERS'
    DCAP_NONSPATIAL = 'DCAP_NONSPATIAL'
    DCAP_NOTNULL_FIELDS = 'DCAP_NOTNULL_FIELDS'
    DCAP_NOTNULL_GEOMFIELDS = 'DCAP_NOTNULL_GEOMFIELDS'
    DCAP_OPEN = 'DCAP_OPEN'
    DCAP_RASTER = 'DCAP_RASTER'
    DCAP_RELATIONSHIPS = 'DCAP_RELATIONSHIPS'
    DCAP_RENAME_LAYERS = 'DCAP_RENAME_LAYERS'
    DCAP_REORDER_FIELDS = 'DCAP_REORDER_FIELDS'
    DCAP_SUBCREATECOPY = 'DCAP_SUBCREATECOPY'
    DCAP_UNIQUE_FIELDS = 'DCAP_UNIQUE_FIELDS'
    DCAP_UPDATE = 'DCAP_UPDATE'
    DCAP_UPSERT = 'DCAP_UPSERT'
    DCAP_VECTOR = 'DCAP_VECTOR'
    DCAP_VIRTUALIO = 'DCAP_VIRTUALIO'
    DCAP_Z_GEOMETRIES = 'DCAP_Z_GEOMETRIES'
    DCAP_MULTIPLE_VECTOR_LAYERS_IN_DIRECTORY = 'GDAL_DCAP_MULTIPLE_VECTOR_LAYERS_IN_DIRECTORY'


class DIM_TYPE(enum.Enum):
    DIM_TYPE_HORIZONTAL_X = 'HORIZONTAL_X'
    DIM_TYPE_HORIZONTAL_Y = 'HORIZONTAL_Y'
    DIM_TYPE_PARAMETRIC = 'PARAMETRIC'
    DIM_TYPE_TEMPORAL = 'TEMPORAL'
    DIM_TYPE_VERTICAL = 'VERTICAL'


class DMD(enum.Enum):
    DMD_ALTER_GEOM_FIELD_DEFN_FLAGS = 'DMD_ALTER_GEOM_FIELD_DEFN_FLAGS'
    DMD_CONNECTION_PREFIX = 'DMD_CONNECTION_PREFIX'
    DMD_CREATIONDATATYPES = 'DMD_CREATIONDATATYPES'
    DMD_CREATIONFIELDDATASUBTYPES = 'DMD_CREATIONFIELDDATASUBTYPES'
    DMD_CREATIONFIELDDATATYPES = 'DMD_CREATIONFIELDDATATYPES'
    DMD_CREATIONOPTIONLIST = 'DMD_CREATIONOPTIONLIST'
    DMD_CREATION_FIELD_DEFN_FLAGS = 'DMD_CREATION_FIELD_DEFN_FLAGS'
    DMD_CREATION_FIELD_DOMAIN_TYPES = 'DMD_CREATION_FIELD_DOMAIN_TYPES'
    DMD_EXTENSION = 'DMD_EXTENSION'
    DMD_EXTENSIONS = 'DMD_EXTENSIONS'
    DMD_HELPTOPIC = 'DMD_HELPTOPIC'
    DMD_LONGNAME = 'DMD_LONGNAME'
    DMD_MAX_STRING_LENGTH = 'DMD_MAX_STRING_LENGTH'
    DMD_MIMETYPE = 'DMD_MIMETYPE'
    DMD_MULTIDIM_ARRAY_CREATIONOPTIONLIST = 'DMD_MULTIDIM_ARRAY_CREATIONOPTIONLIST'
    DMD_MULTIDIM_ARRAY_OPENOPTIONLIST = 'DMD_MULTIDIM_ARRAY_OPENOPTIONLIST'
    DMD_MULTIDIM_ATTRIBUTE_CREATIONOPTIONLIST = 'DMD_MULTIDIM_ATTRIBUTE_CREATIONOPTIONLIST'
    DMD_MULTIDIM_DATASET_CREATIONOPTIONLIST = 'DMD_MULTIDIM_DATASET_CREATIONOPTIONLIST'
    DMD_MULTIDIM_DIMENSION_CREATIONOPTIONLIST = 'DMD_MULTIDIM_DIMENSION_CREATIONOPTIONLIST'
    DMD_MULTIDIM_GROUP_CREATIONOPTIONLIST = 'DMD_MULTIDIM_GROUP_CREATIONOPTIONLIST'
    DMD_NUMERIC_FIELD_WIDTH_INCLUDES_DECIMAL_SEPARATOR = 'DMD_NUMERIC_FIELD_WIDTH_INCLUDES_DECIMAL_SEPARATOR'
    DMD_NUMERIC_FIELD_WIDTH_INCLUDES_SIGN = 'DMD_NUMERIC_FIELD_WIDTH_INCLUDES_SIGN'
    DMD_OPENOPTIONLIST = 'DMD_OPENOPTIONLIST'
    DMD_OVERVIEW_CREATIONOPTIONLIST = 'DMD_OVERVIEW_CREATIONOPTIONLIST'
    DMD_SUBDATASETS = 'DMD_SUBDATASETS'
    DMD_SUPPORTED_SQL_DIALECTS = 'DMD_SUPPORTED_SQL_DIALECTS'
    DMD_UPDATE_ITEMS = 'DMD_UPDATE_ITEMS'
    DMD_ALTER_FIELD_DEFN_FLAGS = 'GDAL_DMD_ALTER_FIELD_DEFN_FLAGS'
    DMD_GEOMETRY_FLAGS = 'GDAL_DMD_GEOMETRY_FLAGS'
    DMD_ILLEGAL_FIELD_NAMES = 'GDAL_DMD_ILLEGAL_FIELD_NAMES'


class GAAT(enum.Enum):
    GAAT_BOOLEAN = 0
    GAAT_STRING = 1
    GAAT_INTEGER = 2
    GAAT_REAL = 3
    GAAT_DATASET = 4
    GAAT_STRING_LIST = 5
    GAAT_INTEGER_LIST = 6
    GAAT_REAL_LIST = 7
    GAAT_DATASET_LIST = 8


class GADV(enum.Enum):
    GADV_NAME = 1
    GADV_OBJECT = 2


class GARIO(enum.Enum):
    GARIO_PENDING = 0
    GARIO_UPDATE = 1
    GARIO_ERROR = 2
    GARIO_COMPLETE = 3


class GA(enum.Enum):
    GA_ReadOnly = 0
    GA_Update = 1


class GCI(enum.Enum):
    GCI_Undefined = 0
    GCI_GrayIndex = 1
    GCI_CyanBand = 10
    GCI_MagentaBand = 11
    GCI_YellowBand = 12
    GCI_BlackBand = 13
    GCI_YCbCr_YBand = 14
    GCI_YCbCr_CbBand = 15
    GCI_YCbCr_CrBand = 16
    GCI_PanBand = 17
    GCI_CoastalBand = 18
    GCI_RedEdgeBand = 19
    GCI_PaletteIndex = 2
    GCI_IR_Start = 20
    GCI_SWIRBand = 21
    GCI_MWIRBand = 22
    GCI_LWIRBand = 23
    GCI_TIRBand = 24
    GCI_OtherIRBand = 25
    GCI_IR_End = 29
    GCI_RedBand = 3
    GCI_SAR_Ka_Band = 30
    GCI_SAR_K_Band = 31
    GCI_SAR_Ku_Band = 32
    GCI_SAR_X_Band = 33
    GCI_SAR_C_Band = 34
    GCI_SAR_S_Band = 35
    GCI_SAR_L_Band = 36
    GCI_SAR_P_Band = 37
    GCI_Max = 39
    GCI_GreenBand = 4
    GCI_BlueBand = 5
    GCI_AlphaBand = 6
    GCI_HueBand = 7
    GCI_SaturationBand = 8
    GCI_LightnessBand = 9


class GDAL_DATA_COVERAGE(enum.Enum):
    GDAL_DATA_COVERAGE_STATUS_UNIMPLEMENTED = 1
    GDAL_DATA_COVERAGE_STATUS_DATA = 2
    GDAL_DATA_COVERAGE_STATUS_EMPTY = 4


class GDAL_DCAP(enum.Enum):
    GDAL_DCAP_CREATE_RELATIONSHIP = 'DCAP_CREATE_RELATIONSHIP'
    GDAL_DCAP_DELETE_RELATIONSHIP = 'DCAP_DELETE_RELATIONSHIP'
    GDAL_DCAP_UPDATE_RELATIONSHIP = 'DCAP_UPDATE_RELATIONSHIP'


class GDAL_DMD(enum.Enum):
    GDAL_DMD_RELATIONSHIP_FLAGS = 'GDAL_DMD_RELATIONSHIP_FLAGS'
    GDAL_DMD_RELATIONSHIP_RELATED_TABLE_TYPES = 'GDAL_DMD_RELATIONSHIP_RELATED_TABLE_TYPES'


class GDT(enum.Enum):
    GDT_Unknown = 0
    GDT_Byte = 1
    GDT_CFloat32 = 10
    GDT_CFloat64 = 11
    GDT_UInt64 = 12
    GDT_Int64 = 13
    GDT_Int8 = 14
    GDT_Float16 = 15
    GDT_CFloat16 = 16
    GDT_TypeCount = 17
    GDT_UInt16 = 2
    GDT_Int16 = 3
    GDT_UInt32 = 4
    GDT_Int32 = 5
    GDT_Float32 = 6
    GDT_Float64 = 7
    GDT_CInt16 = 8
    GDT_CInt32 = 9


class GDsC(enum.Enum):
    GDsCAddRelationship = 'AddRelationship'
    GDsCDeleteRelationship = 'DeleteRelationship'
    GDsCFastGetExtent = 'FastGetExtent'
    GDsCFastGetExtentWGS84LongLat = 'FastGetExtentWGS84LongLat'
    GDsCUpdateRelationship = 'UpdateRelationship'


class GEDTC(enum.Enum):
    GEDTC_NUMERIC = 0
    GEDTC_STRING = 1
    GEDTC_COMPOUND = 2


class GEDTST(enum.Enum):
    GEDTST_NONE = 0
    GEDTST_JSON = 1


class GF(enum.Enum):
    GFT_Integer = 0
    GFT_Real = 1
    GFU_RedMin = 10
    GFU_GreenMin = 11
    GFU_BlueMin = 12
    GFU_AlphaMin = 13
    GFU_RedMax = 14
    GFU_GreenMax = 15
    GFU_BlueMax = 16
    GFU_AlphaMax = 17
    GFU_MaxCount = 18
    GFT_String = 2
    GFT_Boolean = 3
    GFT_DateTime = 4
    GFT_WKBGeometry = 5
    GFU_Red = 6
    GFU_Green = 7
    GFU_Blue = 8
    GFU_Alpha = 9


class GMF(enum.Enum):
    GMF_ALL_VALID = 1
    GMF_PER_DATASET = 2
    GMF_ALPHA = 4
    GMF_NODATA = 8


class GPI(enum.Enum):
    GPI_Gray = 0
    GPI_RGB = 1
    GPI_CMYK = 2
    GPI_HLS = 3


class GRA(enum.Enum):
    GRA_NearestNeighbour = 0
    GRA_Bilinear = 1
    GRA_Med = 10
    GRA_Q1 = 11
    GRA_Q3 = 12
    GRA_Sum = 13
    GRA_RMS = 14
    GRA_Cubic = 2
    GRA_CubicSpline = 3
    GRA_Lanczos = 4
    GRA_Average = 5
    GRA_Mode = 6
    GRA_Max = 8
    GRA_Min = 9


class GRC(enum.Enum):
    GRC_ONE_TO_ONE = 0
    GRC_ONE_TO_MANY = 1
    GRC_MANY_TO_ONE = 2
    GRC_MANY_TO_MANY = 3


class GRIORA(enum.Enum):
    GRIORA_NearestNeighbour = 0
    GRIORA_Bilinear = 1
    GRIORA_RMS = 14
    GRIORA_Cubic = 2
    GRIORA_CubicSpline = 3
    GRIORA_Lanczos = 4
    GRIORA_Average = 5
    GRIORA_Mode = 6
    GRIORA_Gauss = 7


class GRT(enum.Enum):
    GRTT_THEMATIC = 0
    GRTT_ATHEMATIC = 1
    GRT_AGGREGATION = 2


class GTO(enum.Enum):
    GTO_TIP = 0
    GTO_BIT = 1
    GTO_BSQ = 2


class GVM(enum.Enum):
    GVM_Diagonal = 1
    GVM_Edge = 2
    GVM_Max = 3
    GVM_Min = 4


class GVOT(enum.Enum):
    GVOT_NORMAL = 1
    GVOT_MIN_TARGET_HEIGHT_FROM_DEM = 2
    GVOT_MIN_TARGET_HEIGHT_FROM_GROUND = 3


class OF(enum.Enum):
    OFDMP_DEFAULT_VALUE = 0
    OFDMP_SUM = 1
    OFTTime = 10
    OFTDateTime = 11
    OFTInteger64 = 12
    OFTInteger64List = 13
    OFDMP_GEOMETRY_WEIGHTED = 2
    OFSTFloat32 = 3
    OFSTJSON = 4
    OFSTUUID = 5
    OFTWideString = 6
    OFTWideStringList = 7
    OFTBinary = 8
    OFTDate = 9


class VSI(enum.Enum):
    VSI_RANGE_STATUS_UNKNOWN = 0
    VSI_RANGE_STATUS_DATA = 1
    VSI_STAT_CACHE_ONLY = 16
    VSI_RANGE_STATUS_HOLE = 2
    VSI_STAT_SIZE_FLAG = 4
    VSI_STAT_SET_ERROR_FLAG = 8


class ALTER(enum.Enum):
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
    ALTER_GEOM_FIELD_DEFN_TYPE_FLAG = 8192


class F_VAL(enum.Enum):
    F_VAL_ALL = -1
    F_VAL_NULL = 1
    F_VAL_GEOM_TYPE = 2
    F_VAL_WIDTH = 4
    F_VAL_ALLOW_NULL_WHEN_DEFAULT = 8


class GEOS_PREC(enum.Enum):
    GEOS_PREC_NO_TOPO = 1
    GEOS_PREC_KEEP_COLLAPSED = 2


class GGT(enum.Enum):
    GGT_COUNT_NOT_NEEDED = 1
    GGT_STOP_IF_MIXED = 2
    GGT_GEOMCOLLECTIONZ_TINZ = 4


class ODrC(enum.Enum):
    ODrCCreateDataSource = 'CreateDataSource'
    ODrCDeleteDataSource = 'DeleteDataSource'


class ODsC(enum.Enum):
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


class OGRERR(enum.Enum):
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


class OJ(enum.Enum):
    OJUndefined = 0
    OJLeft = 1
    OJRight = 2


class OLC(enum.Enum):
    OLCAlterFieldDefn = 'AlterFieldDefn'
    OLCAlterGeomFieldDefn = 'AlterGeomFieldDefn'
    OLCCreateField = 'CreateField'
    OLCCreateGeomField = 'CreateGeomField'
    OLCCurveGeometries = 'CurveGeometries'
    OLCDeleteFeature = 'DeleteFeature'
    OLCDeleteField = 'DeleteField'
    OLCFastFeatureCount = 'FastFeatureCount'
    OLCFastGetArrowStream = 'FastGetArrowStream'
    OLCFastGetExtent = 'FastGetExtent'
    OLCFastGetExtent3D = 'FastGetExtent3D'
    OLCFastSetNextByIndex = 'FastSetNextByIndex'
    OLCFastSpatialFilter = 'FastSpatialFilter'
    OLCFastWriteArrowBatch = 'FastWriteArrowBatch'
    OLCIgnoreFields = 'IgnoreFields'
    OLCMeasuredGeometries = 'MeasuredGeometries'
    OLCRandomRead = 'RandomRead'
    OLCRandomWrite = 'RandomWrite'
    OLCRename = 'Rename'
    OLCReorderFields = 'ReorderFields'
    OLCSequentialWrite = 'SequentialWrite'
    OLCStringsAsUTF8 = 'StringsAsUTF8'
    OLCTransactions = 'Transactions'
    OLCUpdateFeature = 'UpdateFeature'
    OLCUpsertFeature = 'UpsertFeature'
    OLCZGeometries = 'ZGeometries'


class OLMD(enum.Enum):
    OLMD_FID64 = 'OLMD_FID64'


class TZFLAG(enum.Enum):
    TZFLAG_UNKNOWN = 0
    TZFLAG_LOCALTIME = 1
    TZFLAG_UTC = 100
    TZFLAG_MIXED_TZ = 2


class wkb(enum.Enum):
    wkbGeometryCollection25D = -2147483641
    wkbMultiPolygon25D = -2147483642
    wkbMultiLineString25D = -2147483643
    wkbMultiPoint25D = -2147483644
    wkbPolygon25D = -2147483645
    wkbLineString25D = -2147483646
    wkbPoint25D = -2147483647
    wkb25Bit = -2147483648
    wkbUnknown = 0
    wkbNDR = 1
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


class OAMS(enum.Enum):
    OAMS_TRADITIONAL_GIS_ORDER = 0
    OAMS_AUTHORITY_COMPLIANT = 1
    OAMS_CUSTOM = 2


class OAO(enum.Enum):
    OAO_Other = 0
    OAO_North = 1
    OAO_South = 2
    OAO_East = 3
    OAO_West = 4
    OAO_Up = 5
    OAO_Down = 6


class OSR_CRS_TYPE(enum.Enum):
    OSR_CRS_TYPE_GEOGRAPHIC_2D = 0
    OSR_CRS_TYPE_GEOGRAPHIC_3D = 1
    OSR_CRS_TYPE_GEOCENTRIC = 2
    OSR_CRS_TYPE_PROJECTED = 3
    OSR_CRS_TYPE_VERTICAL = 4
    OSR_CRS_TYPE_COMPOUND = 5
    OSR_CRS_TYPE_OTHER = 6


class PROJ_ERR(enum.Enum):
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


class SRS_DN(enum.Enum):
    SRS_DN_NAD27 = 'North_American_Datum_1927'
    SRS_DN_NAD83 = 'North_American_Datum_1983'
    SRS_DN_WGS72 = 'WGS_1972'
    SRS_DN_WGS84 = 'WGS_1984'


class SRS(enum.Enum):
    SRS_PM_GREENWICH = 'Greenwich'


class SRS_PP(enum.Enum):
    SRS_PP_LATITUDE_OF_1ST_POINT = 'Latitude_Of_1st_Point'
    SRS_PP_LATITUDE_OF_2ND_POINT = 'Latitude_Of_2nd_Point'
    SRS_PP_LONGITUDE_OF_1ST_POINT = 'Longitude_Of_1st_Point'
    SRS_PP_LONGITUDE_OF_2ND_POINT = 'Longitude_Of_2nd_Point'
    SRS_PP_AZIMUTH = 'azimuth'
    SRS_PP_CENTRAL_MERIDIAN = 'central_meridian'
    SRS_PP_FALSE_EASTING = 'false_easting'
    SRS_PP_FALSE_NORTHING = 'false_northing'
    SRS_PP_FIPSZONE = 'fipszone'
    SRS_PP_LANDSAT_NUMBER = 'landsat_number'
    SRS_PP_LATITUDE_OF_CENTER = 'latitude_of_center'
    SRS_PP_LATITUDE_OF_ORIGIN = 'latitude_of_origin'
    SRS_PP_LATITUDE_OF_POINT_1 = 'latitude_of_point_1'
    SRS_PP_LATITUDE_OF_POINT_2 = 'latitude_of_point_2'
    SRS_PP_LATITUDE_OF_POINT_3 = 'latitude_of_point_3'
    SRS_PP_LONGITUDE_OF_CENTER = 'longitude_of_center'
    SRS_PP_LONGITUDE_OF_ORIGIN = 'longitude_of_origin'
    SRS_PP_LONGITUDE_OF_POINT_1 = 'longitude_of_point_1'
    SRS_PP_LONGITUDE_OF_POINT_2 = 'longitude_of_point_2'
    SRS_PP_LONGITUDE_OF_POINT_3 = 'longitude_of_point_3'
    SRS_PP_PATH_NUMBER = 'path_number'
    SRS_PP_PEG_POINT_HEADING = 'peg_point_heading'
    SRS_PP_PEG_POINT_HEIGHT = 'peg_point_height'
    SRS_PP_PEG_POINT_LATITUDE = 'peg_point_latitude'
    SRS_PP_PEG_POINT_LONGITUDE = 'peg_point_longitude'
    SRS_PP_PERSPECTIVE_POINT_HEIGHT = 'perspective_point_height'
    SRS_PP_PSEUDO_STD_PARALLEL_1 = 'pseudo_standard_parallel_1'
    SRS_PP_RECTIFIED_GRID_ANGLE = 'rectified_grid_angle'
    SRS_PP_SATELLITE_HEIGHT = 'satellite_height'
    SRS_PP_SCALE_FACTOR = 'scale_factor'
    SRS_PP_STANDARD_PARALLEL_1 = 'standard_parallel_1'
    SRS_PP_STANDARD_PARALLEL_2 = 'standard_parallel_2'
    SRS_PP_ZONE = 'zone'


class SRS_PT(enum.Enum):
    SRS_PT_AITOFF = 'Aitoff'
    SRS_PT_ALBERS_CONIC_EQUAL_AREA = 'Albers_Conic_Equal_Area'
    SRS_PT_AZIMUTHAL_EQUIDISTANT = 'Azimuthal_Equidistant'
    SRS_PT_BONNE = 'Bonne'
    SRS_PT_CASSINI_SOLDNER = 'Cassini_Soldner'
    SRS_PT_CRASTER_PARABOLIC = 'Craster_Parabolic'
    SRS_PT_CYLINDRICAL_EQUAL_AREA = 'Cylindrical_Equal_Area'
    SRS_PT_ECKERT_I = 'Eckert_I'
    SRS_PT_ECKERT_II = 'Eckert_II'
    SRS_PT_ECKERT_III = 'Eckert_III'
    SRS_PT_ECKERT_IV = 'Eckert_IV'
    SRS_PT_ECKERT_V = 'Eckert_V'
    SRS_PT_ECKERT_VI = 'Eckert_VI'
    SRS_PT_EQUIDISTANT_CONIC = 'Equidistant_Conic'
    SRS_PT_EQUIRECTANGULAR = 'Equirectangular'
    SRS_PT_GALL_STEREOGRAPHIC = 'Gall_Stereographic'
    SRS_PT_GAUSSSCHREIBERTMERCATOR = 'Gauss_Schreiber_Transverse_Mercator'
    SRS_PT_GEOSTATIONARY_SATELLITE = 'Geostationary_Satellite'
    SRS_PT_GNOMONIC = 'Gnomonic'
    SRS_PT_GOODE_HOMOLOSINE = 'Goode_Homolosine'
    SRS_PT_HOTINE_OBLIQUE_MERCATOR = 'Hotine_Oblique_Mercator'
    SRS_PT_HOTINE_OBLIQUE_MERCATOR_AZIMUTH_CENTER = 'Hotine_Oblique_Mercator_Azimuth_Center'
    SRS_PT_HOTINE_OBLIQUE_MERCATOR_TWO_POINT_NATURAL_ORIGIN = 'Hotine_Oblique_Mercator_Two_Point_Natural_Origin'
    SRS_PT_IMW_POLYCONIC = 'International_Map_of_the_World_Polyconic'
    SRS_PT_IGH = 'Interrupted_Goode_Homolosine'
    SRS_PT_KROVAK = 'Krovak'
    SRS_PT_LABORDE_OBLIQUE_MERCATOR = 'Laborde_Oblique_Mercator'
    SRS_PT_LAMBERT_AZIMUTHAL_EQUAL_AREA = 'Lambert_Azimuthal_Equal_Area'
    SRS_PT_LAMBERT_CONFORMAL_CONIC_1SP = 'Lambert_Conformal_Conic_1SP'
    SRS_PT_LAMBERT_CONFORMAL_CONIC_2SP = 'Lambert_Conformal_Conic_2SP'
    SRS_PT_LAMBERT_CONFORMAL_CONIC_2SP_BELGIUM = 'Lambert_Conformal_Conic_2SP_Belgium'
    SRS_PT_LOXIMUTHAL = 'Loximuthal'
    SRS_PT_MERCATOR_1SP = 'Mercator_1SP'
    SRS_PT_MERCATOR_2SP = 'Mercator_2SP'
    SRS_PT_MERCATOR_AUXILIARY_SPHERE = 'Mercator_Auxiliary_Sphere'
    SRS_PT_MILLER_CYLINDRICAL = 'Miller_Cylindrical'
    SRS_PT_MOLLWEIDE = 'Mollweide'
    SRS_PT_NEW_ZEALAND_MAP_GRID = 'New_Zealand_Map_Grid'
    SRS_PT_OBLIQUE_STEREOGRAPHIC = 'Oblique_Stereographic'
    SRS_PT_ORTHOGRAPHIC = 'Orthographic'
    SRS_PT_POLAR_STEREOGRAPHIC = 'Polar_Stereographic'
    SRS_PT_POLYCONIC = 'Polyconic'
    SRS_PT_QSC = 'Quadrilateralized_Spherical_Cube'
    SRS_PT_QUARTIC_AUTHALIC = 'Quartic_Authalic'
    SRS_PT_ROBINSON = 'Robinson'
    SRS_PT_SINUSOIDAL = 'Sinusoidal'
    SRS_PT_SCH = 'Spherical_Cross_Track_Height'
    SRS_PT_STEREOGRAPHIC = 'Stereographic'
    SRS_PT_SWISS_OBLIQUE_CYLINDRICAL = 'Swiss_Oblique_Cylindrical'
    SRS_PT_TRANSVERSE_MERCATOR = 'Transverse_Mercator'
    SRS_PT_TRANSVERSE_MERCATOR_MI_21 = 'Transverse_Mercator_MapInfo_21'
    SRS_PT_TRANSVERSE_MERCATOR_MI_22 = 'Transverse_Mercator_MapInfo_22'
    SRS_PT_TRANSVERSE_MERCATOR_MI_23 = 'Transverse_Mercator_MapInfo_23'
    SRS_PT_TRANSVERSE_MERCATOR_MI_24 = 'Transverse_Mercator_MapInfo_24'
    SRS_PT_TRANSVERSE_MERCATOR_MI_25 = 'Transverse_Mercator_MapInfo_25'
    SRS_PT_TRANSVERSE_MERCATOR_SOUTH_ORIENTED = 'Transverse_Mercator_South_Orientated'
    SRS_PT_TUNISIA_MINING_GRID = 'Tunisia_Mining_Grid'
    SRS_PT_TWO_POINT_EQUIDISTANT = 'Two_Point_Equidistant'
    SRS_PT_VANDERGRINTEN = 'VanDerGrinten'
    SRS_PT_WAGNER_I = 'Wagner_I'
    SRS_PT_WAGNER_II = 'Wagner_II'
    SRS_PT_WAGNER_III = 'Wagner_III'
    SRS_PT_WAGNER_IV = 'Wagner_IV'
    SRS_PT_WAGNER_V = 'Wagner_V'
    SRS_PT_WAGNER_VI = 'Wagner_VI'
    SRS_PT_WAGNER_VII = 'Wagner_VII'
    SRS_PT_WINKEL_I = 'Winkel_I'
    SRS_PT_WINKEL_II = 'Winkel_II'
    SRS_PT_WINKEL_TRIPEL = 'Winkel_Tripel'


class SRS_UA(enum.Enum):
    SRS_UA_DEGREE_CONV = '0.0174532925199433'
    SRS_UA_DEGREE = 'degree'
    SRS_UA_RADIAN = 'radian'


class SRS_UL(enum.Enum):
    SRS_UL_MILLIMETER_CONV = '0.001'
    SRS_UL_CENTIMETER_CONV = '0.01'
    SRS_UL_INTL_INCH_CONV = '0.0254'
    SRS_UL_US_INCH_CONV = '0.025400050800101603'
    SRS_UL_DECIMETER_CONV = '0.1'
    SRS_UL_LINK_Clarke_CONV = '0.2011661949'
    SRS_UL_LINK_CONV = '0.20116684023368047'
    SRS_UL_INTL_LINK_CONV = '0.201168'
    SRS_UL_INDIAN_FOOT_CONV = '0.30479841'
    SRS_UL_FOOT_CONV = '0.3048'
    SRS_UL_US_FOOT_CONV = '0.3048006096012192'
    SRS_UL_INDIAN_YARD_CONV = '0.91439523'
    SRS_UL_INTL_YARD_CONV = '0.9144'
    SRS_UL_US_YARD_CONV = '0.914401828803658'
    SRS_UL_INTL_FATHOM_CONV = '1.8288'
    SRS_UL_KILOMETER_CONV = '1000.'
    SRS_UL_INTL_STAT_MILE_CONV = '1609.344'
    SRS_UL_US_STAT_MILE_CONV = '1609.347218694437'
    SRS_UL_INTL_NAUT_MILE_CONV = '1852.0'
    SRS_UL_CHAIN_CONV = '20.116684023368047'
    SRS_UL_INDIAN_CHAIN_CONV = '20.11669506'
    SRS_UL_INTL_CHAIN_CONV = '20.1168'
    SRS_UL_US_CHAIN_CONV = '20.11684023368047'
    SRS_UL_ROD_CONV = '5.02921005842012'
    SRS_UL_CENTIMETER = 'Centimeter'
    SRS_UL_CHAIN = 'Chain'
    SRS_UL_INDIAN_CHAIN = 'Chain_Indian'
    SRS_UL_INTL_CHAIN = 'Chain_International'
    SRS_UL_US_CHAIN = 'Chain_US_Surveyor'
    SRS_UL_DECIMETER = 'Decimeter'
    SRS_UL_INTL_FATHOM = 'Fathom_International'
    SRS_UL_FOOT = 'Foot (International)'
    SRS_UL_INDIAN_FOOT = 'Foot_Indian'
    SRS_UL_INTL_FOOT = 'Foot_International'
    SRS_UL_US_FOOT = 'Foot_US'
    SRS_UL_INTL_INCH = 'Inch_International'
    SRS_UL_US_INCH = 'Inch_US_Surveyor'
    SRS_UL_KILOMETER = 'Kilometer'
    SRS_UL_LINK = 'Link'
    SRS_UL_LINK_Clarke = 'Link_Clarke'
    SRS_UL_INTL_LINK = 'Link_International'
    SRS_UL_METER = 'Meter'
    SRS_UL_MILLIMETER = 'Millimeter'
    SRS_UL_NAUTICAL_MILE = 'Nautical Mile'
    SRS_UL_INTL_NAUT_MILE = 'Nautical_Mile_International'
    SRS_UL_ROD = 'Rod'
    SRS_UL_INTL_STAT_MILE = 'Statute_Mile_International'
    SRS_UL_US_STAT_MILE = 'Statute_Mile_US_Surveyor'
    SRS_UL_INDIAN_YARD = 'Yard_Indian'
    SRS_UL_INTL_YARD = 'Yard_International'
    SRS_UL_US_YARD = 'Yard_US_Surveyor'


class SRS_WGS84(enum.Enum):
    SRS_WGS84_INVFLATTENING = 298.257223563
    SRS_WGS84_SEMIMAJOR = 6378137.0


class SRS_WKT(enum.Enum):
    SRS_WKT_WGS84_LAT_LONG = 'GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AXIS["Latitude",NORTH],AXIS["Longitude",EAST],AUTHORITY["EPSG","4326"]]'


class GAT(enum.Enum):
    GATDijkstraShortestPath = 1
    GATKShortestPath = 2
    GATConnectedComponents = 3


class GNM_EDGE_DIR(enum.Enum):
    GNM_EDGE_DIR_BOTH = 0
    GNM_EDGE_DIR_SRCTOTGT = 1
    GNM_EDGE_DIR_TGTTOSRC = 2


