import os
import sys
import urllib.request
import re

# PREWORK (don't modify): import colors, save to temp file and import
tmp = os.getenv("TMP", "/tmp")
color_values_module = os.path.join(tmp, "color_values.py")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/color_values.py", color_values_module
)
sys.path.append(tmp)

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color):
        self.color = color
        try:
            self.rgb = COLOR_NAMES[str(color).upper()]
        except KeyError:
            self.rgb = None

    @staticmethod
    def _validate_rbg(color: tuple[int, int, int]):
        """Validates if color is a valid rgb tuple"""

        err_msg = "must be tuple(int,int,int) with int values in Range(0,256)"
        if not isinstance(color, tuple):
            raise ValueError(err_msg)
        elif not all([0 <= value <= 255 for value in color]):
            raise ValueError(err_msg)

    @staticmethod
    def _validate_hex(color: str):
        err_msg = "Input must be hex value."
        if not re.match("^#[a-f0-9]{6}$", color):
            raise ValueError(err_msg)

    @staticmethod
    def hex2rgb(hex):
        """Class method that converts a hex value into an rgb one"""
        Color._validate_hex(hex)
        return (int(hex[1:3], 16), int(hex[3:5], 16), int(hex[5:7], 16))

    @staticmethod
    def rgb2hex(rgb: tuple[int, int, int]) -> str:
        """Class method that converts an rgb value into a hex one"""
        Color._validate_rbg(rgb)
        return "#" + ("".join(f"{rgb[i]:02x}" for i in range(0, 3)))

    def __repr__(self):
        """Returns the repl of the object"""
        return f"Color('{self.color}')"

    def __str__(self):
        """Returns the string value of the color object"""
        return f"{self.rgb}" if self.rgb else "Unknown"
