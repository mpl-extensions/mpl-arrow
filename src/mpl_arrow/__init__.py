"""Easily plot nice-looking arrows with matplotlib."""
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("mpl-arrow")
except PackageNotFoundError:
    __version__ = "uninstalled"

__author__ = "Kevin M. Dalton, Ian Hunt-Isaak"
__email__ = "kevinmdalton@gmail.com, ianhuntisaak@gmail.com"

from ._arrow import arrow, arrow_absolute, vector

__all__ = [
    "arrow",
    "arrow_absolute",
    "vector",
]
