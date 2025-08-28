from enum import IntEnum,StrEnum

# Gender enumeration
class Gender(IntEnum):
    MALE = 1
    FEMALE = 2
    OTHER = 3

    @classmethod
    def choices(cls):
        return [(member.value, member.name.capitalize()) for member in cls]

# User role enumeration
class Role(IntEnum):
    ENDUSER_CUSTOMER = 1
    ENDUSER_STAFF = 2
    ADMIN = 3

    @classmethod
    def choices(cls):
        return [(key.value, key.name.replace("_", " ").title()) for key in cls]


# Account status enumeration
class Status(StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"
    SUSPENDED = "suspended"


# Order status enumeration
class OrderStatus(StrEnum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

