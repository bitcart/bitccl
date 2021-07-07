import ast
import builtins
import functools
import inspect
import warnings

from RestrictedPython import RestrictingNodeTransformer
from RestrictedPython.Eval import default_guarded_getitem, default_guarded_getiter
from RestrictedPython.Guards import full_write_guard, guarded_iter_unpack_sequence, guarded_unpack_sequence
from RestrictedPython.Guards import safe_builtins as safe_builtins_default
from RestrictedPython.Guards import safer_getattr as _restricted_getattr
from RestrictedPython.Utilities import utility_builtins

from bitccl import events as events_module
from bitccl import functions as functions_module
from bitccl.exceptions import CompilationRestrictedError
from bitccl.utils import no_imports_importer

functions = {
    name: func for (name, func) in inspect.getmembers(functions_module, inspect.isfunction) if hasattr(func, "bitccl")
}
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

    def visit_AugAssign(self, node):
        node = self.node_contents_visit(node)
        return node

    def visit_AsyncFunctionDef(self, node):
        return self.node_contents_visit(node)

    def visit_Await(self, node):
        return self.node_contents_visit(node)

    def visit_AsyncFor(self, node):
        return self.node_contents_visit(node)

    def visit_AsyncWith(self, node):
        return self.node_contents_visit(node)


def _metaclass(name, bases, dict):
    obj = type(name, bases, dict)
    obj._guarded_writes = 1
    return obj


_safe_names = [
    "next",
    "iter",
    "filter",
    "max",
    "min",
    "map",
    "zip",
    "list",
    "dict",
    "enumerate",
    "sum",
    "any",
    "all",
]
_safe_exceptions = [
    "StopAsyncIteration",
]

safe_builtins = safe_builtins_default.copy()
safe_builtins.update(utility_builtins)

for name in _safe_names:
    safe_builtins[name] = getattr(builtins, name)

for name in _safe_exceptions:
    safe_builtins[name] = getattr(builtins, name)

safe_builtins["reduce"] = functools.reduce
safe_builtins["__import__"] = no_imports_importer


def guarded_hasattr(obj, name):
    try:
        safer_getattr(obj, name)
    except (AttributeError, TypeError):
        return False
    return True


safe_builtins["hasattr"] = guarded_hasattr


SENTINEL = object()


def getattr_impl(obj, name, default):
    if default is SENTINEL:
        return getattr(obj, name)
    else:
        return getattr(obj, name, default)


def safer_getattr(obj, name, default=SENTINEL):
    return _restricted_getattr(obj, name, default, getattr=getattr_impl)


def apply(func, *args, **kwargs):
    return func(*args, **kwargs)


safe_globals = {
    **functions,
    **events,
    "print": print,
    "getattr": safer_getattr,
    "__builtins__": safe_builtins,
    "__metaclass__": _metaclass,
    "__name__": "__main__",
    "_apply_": apply,
    "_getitem_": default_guarded_getitem,
    "_getiter_": default_guarded_getiter,
    "_iter_unpack_sequence_": guarded_iter_unpack_sequence,
    "_unpack_sequence_": guarded_unpack_sequence,
    "_write_": full_write_guard,
}


def compile_restricted(source, filename="<string", **kwargs):
    byte_code = None
    collected_errors = []
    collected_warnings = []
    c_ast = ast.parse(source, filename, "exec")
    policy_instance = Policy(collected_errors, collected_warnings, {})
    policy_instance.visit(c_ast)
    if not collected_errors:
        byte_code = compile(c_ast, filename, mode="exec")
    for warning in collected_warnings:  # pragma: no cover
        warnings.warn(warning, SyntaxWarning)
    if collected_errors:
        raise CompilationRestrictedError(collected_errors)
    exec(
        byte_code,
        {**kwargs, **safe_globals},
    )
