from unittest import TestCase
from unittest.mock import Mock

from api.endpoints import GeneratorEndpoint


class EndpointsTest(TestCase):

    def setUp(self):
        self.endpoint = GeneratorEndpoint()

