from unittest import TestCase
from storage_domain.database import loadSession
from storage_domain.dbschema.memes import Memes

from sqlalchemy.exc import OperationalError

class TestDatabase(TestCase):

    def test_app_connects_to_postgres_server(self):

        try:
            session = loadSession()
            session.query(Memes).first()

        except OperationalError:
            self.fail("App failed to connect to PostgreSQL server. \
Please make sure the server is running and \"memegem\" database is present")
