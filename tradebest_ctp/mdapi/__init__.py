"""
Market Data API module for CTP
"""

import os
import platform
import sys

system = platform.system()
machine = platform.machine()
python_version = f"{sys.version_info.major}.{sys.version_info.minor}"

if system == "Windows":
    if machine == "AMD64":
        platform_dir = "win64"
    else:
        platform_dir = "win32"
elif system == "Linux":
    platform_dir = "linux64"
elif system == "Darwin":
    platform_dir = "macosx"
else:
    raise Exception(f"Unsupported platform: {system}")

ctp_versions = [
    "6.3.15_20190220",
    "6.3.19_P1_20200106",
    "6.5.1_20200908",
    "6.6.1_P1_20210406",
    "6.6.7_20220613",
    "6.6.9_20220920",
    "6.7.0_20230209",
    "6.7.1_20230613",
    "6.7.2_20230913",
    "6.7.7_20240607",
]

default_version = ctp_versions[-1]

module_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 
                          default_version, platform_dir)
sys.path.insert(0, module_path)

from thostmduserapi import *

__all__ = [name for name in dir() if not name.startswith('_')]
