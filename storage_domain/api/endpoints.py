from flask.views import MethodView
from flask.json import jsonify

from storage_domain.database import loadSession
from storage_domain.dbschema.memes import Memes


class StorageEndpoint(MethodView):
    methods = ["GET", "POST"]

    def get(self):

        session = loadSession()
        queryset = session.query(Memes).all()

        queryset = [item.serialise() for item in queryset]

        return jsonify(queryset)
