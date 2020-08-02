import inspect
import sys
import traceback

import httpx

from . import events as events_module
from . import functions as functions_module
from . import state
from .utils import disabled_imports, init_base_event, load_config, mark_allowed_imports
from .version import VERSION

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
    http_client = mark_allowed_imports(
        httpx.Client(http2=True, headers={"user-agent": f"bitccl/{VERSION}"})
    )
    try:
        with disabled_imports():
            code = compile(source, filename, "exec")
            exec(
                code,
                {"http": http_client, "http_codes": httpx.codes, **functions, **events},
            )
    except BaseException:
        stack_frames = len(traceback.extract_tb(sys.exc_info()[2])) - 1
        return traceback.format_exc(-stack_frames)
    finally:
        http_client.close()
        state.event_listeners.clear()
