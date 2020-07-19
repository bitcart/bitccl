import inspect
import sys
import traceback

from . import events as events_module
from . import functions as functions_module
from . import state
from .utils import disable_imports, enable_imports, init_base_event, load_config

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


def run(source, filename="<string>", config=None):
    state.config.set(config if config is not None else load_config())
    disable_imports()
    try:
        code = compile(source, filename, "exec")
        exec(code, {**functions, **events})
    except BaseException:
        stack_frames = len(traceback.extract_tb(sys.exc_info()[2])) - 1
        return traceback.format_exc(-stack_frames)
    finally:
        state.event_listeners.clear()
        enable_imports()
