from enum import Enum

class DetailType(Enum):
    ENGINE = 0
    TRANSMISSION = 1
    GAS_PEDAL = 2
    WHEELS = 3
    BODY = 4


class TransmissionType(Enum):
    MANUAL = 0
    AUTOMATIC = 1


class Color(Enum):
    WHITE = 0
    BLACK = 1
    RED = 2
    GREEN = 3
    BLUE = 4