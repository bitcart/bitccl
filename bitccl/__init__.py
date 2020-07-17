import inspect
import sys
import traceback

from . import events as events_module
from . import functions as functions_module
from .utils import init_base_event, no_imports_importer

functions = {
    name: func
    for (name, func) in inspect.getmembers(functions_module, inspect.isfunction)
}
events = {
    name: event
    for (name, event) in inspect.getmembers(events_module, inspect.isclass)
    if issubclass(event, events_module.BaseEvent)
}

init_base_event()


def run(source, filename="<string>"):
    __builtins__["__import__"] = no_imports_importer
    try:
        code = compile(source, filename, "exec")
        exec(code, {**functions, **events})
    except BaseException:
        stack_frames = len(traceback.extract_tb(sys.exc_info()[2])) - 1
        print(traceback.format_exc(-stack_frames), end="")
