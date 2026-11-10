import enum
from typing import Literal

type GNM_EDGE_DIR = Literal[0, 1, 2]


class GNM_EDGE_DIREnum(enum.IntEnum):
    GNM_EDGE_DIR_BOTH = 0
    GNM_EDGE_DIR_SRCTOTGT = 1
    GNM_EDGE_DIR_TGTTOSRC = 2
