import os
import sys

from flask import Flask

from api.endpoints import StorageEndpoint
from api.config import Config


def make_app(test_config=None,
             SECRET_KEY='dev'):
    sys.path.append(os.path.join(__file__, '..', '..'))

    app = Flask(__name__)
    app.config.from_mapping(SECRET_KEY=SECRET_KEY)

    if not test_config:
        app.config.from_object(Config)
    else:
        app.config.from_mapping(test_config)
    app.add_url_rule('/storage/', view_func=StorageEndpoint.as_view('storage_endpoint'))

    return app
