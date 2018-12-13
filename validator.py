from memegen.exceptions import ValidationError


class Validator(object):

    def validate_ratio(self, image_data):

        width = image_data.get('width')
        height = image_data.get('height')
        ratio = width / height
        allowed_ratio_horizontal = 16 / 9
        allowed_ratio_vertical = 9 / 16

        if ratio > allowed_ratio_horizontal or ratio < allowed_ratio_vertical:
            raise ValidationError

        return image_data

    def validate_size(self, image_data):

        width = image_data.get('height')
        height = image_data.get('width')
        size_min = 200
        size_max = 1920

        if width < size_min or height < size_min:
            raise ValidationError

        if width > size_max or height > size_max:
            raise ValidationError

        return image_data
