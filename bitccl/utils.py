import importlib
import inspect
import json
import os
import signal
import traceback
from contextlib import contextmanager

from . import events
from .datatypes import ExtendedDict
from .exceptions import TimeoutException
from .logger import logger


def load_config():  # pragma: no cover
    config = {}
    data = ""
    if not os.path.exists("config.json"):
        logger.debug("No config file existing. No settings set. Some functions might not work properly")
    try:
        with open("config.json") as f:
            data = f.read()
    except OSError:
        logger.debug("Error reading config file")
    try:
        config = json.loads(data)
    except json.JSONDecodeError:
        logger.debug("Invalid json in config file")
    return ExtendedDict(lambda: None, **config)


def silent_debug():
    caller_name = inspect.currentframe().f_back.f_code.co_name
    logger.debug(f"Error in {caller_name}. Traceback:\n{traceback.format_exc()}")


def no_imports_importer(*args, **kwargs):
    raise ImportError("Imports disabled")


def enable_imports():
    __builtins__["__import__"] = importlib.__import__


def disable_imports():
    __builtins__["__import__"] = no_imports_importer


@contextmanager
def disabled_imports():
    disable_imports()
    try:
        yield
    finally:
        enable_imports()


def allow_imports(func):
    def wrapper(*args, **kwargs):
        imported = __builtins__["__import__"]
        enable_imports()
        result = func(*args, **kwargs)
        __builtins__["__import__"] = imported
        return result

    return wrapper


def mark_allowed_imports(obj):
    for method_name in dir(obj):
        if not method_name.startswith("_") and callable(inspect.getattr_static(obj, method_name)):  # to avoid calling props
            setattr(
                obj,
                method_name,
                allow_imports(getattr(obj, method_name)),
            )
    return obj


def prepare_event(event):
    if isinstance(event, str):
        event = getattr(
            events, event, type(event, (events.BaseEvent,), {"name": event})
        )()  # dynamic event class if no event exists
    if inspect.isclass(event) and issubclass(event, events.BaseEvent):
        event = event()
    return event


def init_base_event():
    events.BaseEvent.init_imports()


@contextmanager
def time_limit(seconds):
    def signal_handler(signum, frame):
        raise TimeoutException("Timed out!")

    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)
