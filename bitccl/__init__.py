import inspect
import sys
import traceback

from . import events as events_module
from . import functions as functions_module
from . import plugins as plugins_module
from . import state
from .utils import disabled_imports, init_base_event, load_config
from .version import VERSION

functions = {name: func for (name, func) in inspect.getmembers(functions_module, inspect.isfunction)}
events = {
    name: event
    for (name, event) in inspect.getmembers(events_module, inspect.isclass)
    if issubclass(event, events_module.BaseEvent)
}

init_base_event()


def run(source, filename="<string>", config=None, plugins=[]):
    state.config.set(config if config is not None else load_config())
    context = plugins_module.startup(additional_modules=plugins)
    try:
        with disabled_imports():
            code = compile(source, filename, "exec")
            exec(
                code,
                {**context, **functions, **events},
            )
    except BaseException:
        stack_frames = len(traceback.extract_tb(sys.exc_info()[2])) - 1
        return traceback.format_exc(-stack_frames)
    finally:
        plugins_module.shutdown(context, additional_modules=plugins)
        state.event_listeners.clear()


__all__ = ["run", "VERSION"]
