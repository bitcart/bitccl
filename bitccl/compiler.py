import inspect

from RestrictedPython import RestrictingNodeTransformer
from RestrictedPython import compile_restricted as _compile_source
from RestrictedPython.Guards import full_write_guard
from RestrictedPython.Guards import safe_builtins as safe_builtins_default

from . import events as events_module
from . import functions as functions_module
from .utils import no_imports_importer

functions = {name: func for (name, func) in inspect.getmembers(functions_module, inspect.isfunction)}
events = {
    name: event
    for (name, event) in inspect.getmembers(events_module, inspect.isclass)
    if issubclass(event, events_module.BaseEvent)
}


class Policy(RestrictingNodeTransformer):
    def inject_print_collector(self, node, position=0):
        pass

    def visit_Name(self, node):
        node = self.node_contents_visit(node)
        if node.id != "print":
            self.check_name(node, node.id)
        return node


def _metaclass(name, bases, dict):
    obj = type(name, bases, dict)
    obj.__allow_access_to_unprotected_subobjects__ = 1
    obj._guarded_writes = 1
    return obj


safe_builtins = safe_builtins_default.copy()
safe_builtins["__import__"] = no_imports_importer

safe_globals = {
    **functions,
    **events,
    "print": print,
    "__builtins__": safe_builtins,
    "__metaclass__": _metaclass,
    "__name__": "__main__",
    "_write_": full_write_guard,
}


def compile_restricted(source, filename="<string", **kwargs):
    code = _compile_source(source, filename, "exec", policy=Policy)
    exec(
        code,
        {**kwargs, **safe_globals},
    )
