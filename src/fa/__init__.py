"""
FlashArray Helper Utilities Package
Provides simplified access to FlashArray file and policy management.
"""
__version__ = "0.0.1"

# Import key classes and functions
from .flash_array import (
    FlashArrayError,
    FlashArray
)

__all__ = [
    "FlashArrayError",
    "FlashArray"
]