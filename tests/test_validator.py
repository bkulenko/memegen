from unittest import TestCase
from generator_domain.validator import Validator
from generator_domain.exceptions import ValidationError


class ValidatorTest(TestCase):

    def setUp(self):
        self.validator = Validator()

    def test_validate_ratio(self):
        image_dimensions = {'width': 1920, 'height': 1080}
        validated_data = self.validator.validate_ratio(image_dimensions)
        self.assertEqual(validated_data, image_dimensions)

        image_dimensions = {'width': 800, 'height': 600}
        validated_data = self.validator.validate_ratio(image_dimensions)
        self.assertEqual(validated_data, image_dimensions)

        image_dimensions = {'width': 600, 'height': 600}
        validated_data = self.validator.validate_ratio(image_dimensions)
        self.assertEqual(validated_data, image_dimensions)

        image_dimensions = {'width': 1, 'height': 15000}
        with self.assertRaises(ValidationError):
            validated_data = self.validator.validate_ratio(image_dimensions)

        image_dimensions = {'width': 15000, 'height': 1}
        with self.assertRaises(ValidationError):
            validated_data = self.validator.validate_ratio(image_dimensions)

    def test_validate_size(self):

        image_dimensions = {'width': 500, 'height': 500}
        validated_data = self.validator.validate_size(image_dimensions)
        self.assertEqual(validated_data, image_dimensions)

        image_dimensions = {'width': 1500, 'height': 500}
        validated_data = self.validator.validate_size(image_dimensions)
        self.assertEqual(validated_data, image_dimensions)

        image_dimensions = {'width': 500, 'height': 1500}
        validated_data = self.validator.validate_size(image_dimensions)
        self.assertEqual(validated_data, image_dimensions)

        image_dimensions = {'width': 1, 'height': 15000}
        with self.assertRaises(ValidationError):
            validated_data = self.validator.validate_size(image_dimensions)

        image_dimensions = {'width': 15000, 'height': 1}
        with self.assertRaises(ValidationError):
            validated_data = self.validator.validate_size(image_dimensions)

    def test_validate_mimetype(self):

        image_mime = {'mimetype': 'image/jpeg'}
        validated_data = self.validator.validate_mimetype(image_mime)
        self.assertEqual(validated_data, image_mime)

        image_mime = {'mimetype': 'image/png'}
        validated_data = self.validator.validate_mimetype(image_mime)
        self.assertEqual(validated_data, image_mime)

        image_mime = {'mimetype': 'image/gif'}
        validated_data = self.validator.validate_mimetype(image_mime)
        self.assertEqual(validated_data, image_mime)

        image_mime = {'mimetype': 'image/tiff'}
        with self.assertRaises(ValidationError):
            validated_data = self.validator.validate_mimetype(image_mime)

        image_mime = {'mimetype': 'application/json'}
        with self.assertRaises(ValidationError):
            validated_data = self.validator.validate_mimetype(image_mime)

        image_mime = {'mimetype': 'text/html'}
        with self.assertRaises(ValidationError):
            validated_data = self.validator.validate_mimetype(image_mime)

    def test_validator(self):

        image_data = {
            'mimetype': 'image/jpeg', 
            'width': 800,
            'height': 600,
        }
        try:
            self.validator(image_data)
        except ValidationError:
            self.fail("Validator failed to validate image data!")
