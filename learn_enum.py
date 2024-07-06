from enum import Enum


class Sizes(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


def get_value_from_enum(size: Sizes):
    print(size.name)  # 👉️ MEDIUM
    print(size.value)  # 👉️ 2

    return size.value


result = get_value_from_enum(Sizes.MEDIUM)

print(result)
