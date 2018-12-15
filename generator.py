import base64

from generator_domain.validator import Validator

from io import BytesIO

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


class Generator(object):

    def __init__(self, **kwargs):
        self._validator = Validator()
        self._storage_adapter = kwargs.get("storage_adapter")

    def __call__(self, image_data):
        return self._add_text(image_data)

    def _add_text(self, image_data):
        if not image_data['top_text'] and not image_data['bottom_text']:
            return image_data
        else:
            #font = image_data.get('font')
            image = Image.open(BytesIO(base64.b64decode(image_data.get('base64'))))
            print(image)
            top_text = image_data.get('top_text')
            bottom_text = image_data.get('bottom_text')
            draw = ImageDraw.Draw(image)
            #font = ImageFont.truetype(font, 16)

            draw.text((0, 0), top_text, (255, 255, 255))
            draw.text((0, 150), bottom_text, (255, 255, 255))

            image_processed = base64.b64encode(image)
            image_data["base64"] = image_processed

            return image_data
