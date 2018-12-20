from generator_domain.models import Image

from unittest import TestCase


class TestImageModel(TestCase):

    def test_should_generate_uid(self):
        image = Image()
        self.assertNotEqual(image.uid, None)
        self.assertNotEqual(image.uid, '')
