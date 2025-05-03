"""
Trading API module for CTP
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

version = "6.7.7_20240607"

module_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                          version, platform_dir)
sys.path.insert(0, module_path)

if system == "Windows":
    py_version_dir = f"py3{python_version.split('.')[1]}"
    py_module_path = os.path.join(module_path, py_version_dir)
    if os.path.exists(py_module_path):
        sys.path.insert(0, py_module_path)

if system == "Linux":
    lib_path = os.environ.get("LD_LIBRARY_PATH", "")
    if module_path not in lib_path:
        os.environ["LD_LIBRARY_PATH"] = f"{module_path}:{lib_path}"

from thosttraderapi import *

__all__ = [name for name in dir() if not name.startswith('_')]
