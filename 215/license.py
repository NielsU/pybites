import re


def validate_license(key: str) -> bool:
    """Write a regex that matches a PyBites license key
    (e.g. PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4)
    """

    licence_pattern = re.compile(r"^PB(-(\d|[A-Z]){8}){4}$")
    match = licence_pattern.match(key)

    return True if match else False
