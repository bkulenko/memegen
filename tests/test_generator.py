from unittest import TestCase
from memegen.validator import Validator
from memegen.exceptions import ValidationError


class GeneratorTest(TestCase):

    def test_validate_ratio(self):
        validator = Validator()
        image_dimensions = {'width': 1920, 'height': 1080}
        validated_data = validator.validate_ratio(image_dimensions)
        self.assertEqual(validated_data, image_dimensions)

        image_dimensions = {'width': 800, 'height': 600}
        validated_data = validator.validate_ratio(image_dimensions)
        self.assertEqual(validated_data, image_dimensions)

        image_dimensions = {'width': 600, 'height': 600}
        validated_data = validator.validate_ratio(image_dimensions)
        self.assertEqual(validated_data, image_dimensions)

        image_dimensions = {'width': 1, 'height': 15000}
        with self.assertRaises(ValidationError):
            validated_data = validator.validate_ratio(image_dimensions)

        image_dimensions = {'width': 15000, 'height': 1}
        with self.assertRaises(ValidationError):
            validated_data = validator.validate_ratio(image_dimensions)
