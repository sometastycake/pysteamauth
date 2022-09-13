from enum import IntEnum


class ESessionPersistence(IntEnum):
    k_ESessionPersistence_Invalid: int = -1
    k_ESessionPersistence_Ephemeral: int = 0
    k_ESessionPersistence_Persistent: int = 1
