def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
    boundaries (0, 255) and returns its converted hex, for example:
    Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    hexval = ""
    for nr in rgb:
        if nr < 0 or nr > 255:
            raise ValueError("Value out of bounds min 0, max 255.")

        hexval += f"{nr:02x}"

    return f"#{hexval}".upper()
