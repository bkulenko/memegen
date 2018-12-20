import os
import sys


from flask import Flask

from api.endpoints import GeneratorEndpoint
from api.config import Config


def make_app(test_config=None,
             SECRET_KEY='dev'):

    sys.path.append(os.path.join(__file__, '../../'))
    app = Flask(__name__,)
    app.config.from_mapping(SECRET_KEY=SECRET_KEY)

    if not test_config:
        app.config.from_object(Config)
    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.add_url_rule('/generator/', view_func=GeneratorEndpoint.as_view('generator_endpoint'))

    return app
