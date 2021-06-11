from bitccl.ext import modules


def startup(additional_modules=[]):
    context = {}
    for module in modules + additional_modules:
        context.update(module.startup())
    return context


def shutdown(context, additional_modules=[]):
    for module in modules + additional_modules:
        module.shutdown(context)
