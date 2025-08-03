from enum import IntEnum,StrEnum

class Gender(IntEnum):
    MALE = 1
    FEMALE = 2
    OTHER = 3

    @classmethod
    def choices(cls):
        return [(member.value, member.name.capitalize()) for member in cls]



class Role(IntEnum):
    ENDUSER_CUSTOMER = 1
    ENDUSER_STAFF = 2
    ADMIN = 3

    @classmethod
    def choices(cls):
        return [(key.value, key.name.replace("_", " ").title()) for key in cls]




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

