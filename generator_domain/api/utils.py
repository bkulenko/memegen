from config import Config
from importlib import import_module

import requests


def importer(name, package):
    mod = import_module(name, package)
    return getattr(mod, package)

def poster(data):
    requests.post("{}{}:{}/{}/".format(Config.dbschema, Config.dbhost, Config.dbport, Config.dbendpoint),data)