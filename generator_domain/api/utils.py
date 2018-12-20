from importlib import import_module


def importer(name, package):
    mod = import_module(name, package)
    return getattr(mod, package)
