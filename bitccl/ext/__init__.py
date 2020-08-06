import glob
import importlib
import os

modules = [
    os.path.basename(f)[:-3]  # strip .py
    for f in glob.glob(os.path.join(os.path.dirname(__file__), "*.py"))
    if os.path.isfile(f) and not f.endswith("__init__.py")
]
__all__ = modules
modules = [importlib.import_module(f".{m}", "bitccl.ext") for m in modules]
