import sys
import traceback

from . import plugins as plugins_module
from . import state
from .compiler import compile_restricted
from .utils import init_base_event, load_config
from .version import VERSION

init_base_event()


def run(source, filename="<string>", config=None, plugins=[]):
    state.config.set(config if config is not None else load_config())
    context = plugins_module.startup(additional_modules=plugins)
    try:
        compile_restricted(source, filename, **context)
    except BaseException:
        stack_frames = len(traceback.extract_tb(sys.exc_info()[2])) - 1
        return traceback.format_exc(-stack_frames)
    finally:
        plugins_module.shutdown(context, additional_modules=plugins)
        state.event_listeners.clear()


__all__ = ["run", "VERSION"]
