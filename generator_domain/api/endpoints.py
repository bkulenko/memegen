import json

from flask import request, jsonify

from flask.views import MethodView

from api.config import Config
from api.utils import importer


class GeneratorEndpoint(MethodView):
    methods = ["POST"]

    def __init__(self):
        super().__init__()
        self._validator = importer(**Config.validator_class)()
        self._generator = importer(**Config.generator_class)()
        self._thumbnailer = importer(**Config.thumbnailer_class)()

    def post(self):
        data = json.loads(request.data)
        self._validator(data)
        self._generator(data)
        self._thumbnailer(data)
        return jsonify(data)
