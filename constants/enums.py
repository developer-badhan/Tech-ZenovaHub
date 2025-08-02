from enum import IntEnum,StrEnum

class Gender(IntEnum):
    MALE = 1
    FEMALE = 2
    OTHER = 3

    @classmethod
    def choices(cls):
        return [(member.value, member.name.capitalize()) for member in cls]


class Role(IntEnum):
    ADMIN = 1
    ENDUSER = 2

    @classmethod
    def choices(cls):
        return [(member.value, member.name.capitalize()) for member in cls]



class Status(StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"
    SUSPENDED = "suspended"

class OrderStatus(StrEnum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

