import json

from flask import request, jsonify

from flask.views import MethodView

from api.config import Config
from api.utils import importer, poster

Validator = importer(**Config.validator_class)
Generator = importer(**Config.generator_class)
Thumbnailer = importer(**Config.thumbnailer_class)

class GeneratorEndpoint(MethodView):
    methods = ["POST"]

    def __init__(self):
        super().__init__()
        self._validator = Validator()
        self._generator = Generator()
        self._thumbnailer = Thumbnailer()

    def post(self):
        data = json.loads(request.data)
        self._validator(data)
        self._generator(data)
        self._thumbnailer(data)
        poster(data)
        return jsonify(data)
