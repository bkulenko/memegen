import base64

from generator_domain.validator import Validator

from io import BytesIO

from PIL import Image, ImageFont, ImageDraw


class Generator(object):

    def __init__(self, **kwargs):
        self._validator = Validator()
        self._storage_adapter = kwargs.get("storage_adapter")

    def __call__(self, image_data):
        self._validator(image_data)
        return self._add_text(image_data)

    def _add_text(self, image_data):
            if not image_data.get('top_text') and not image_data.get('bottom_text'):
                return image_data
            else:

                font = image_data.get('font')
                image = Image.open(BytesIO(base64.b64decode(image_data.get('base64'))))
                top_text = image_data.get('top_text')
                bottom_text = image_data.get('bottom_text')
                draw = ImageDraw.Draw(image)
                font_size = 16
                font = ImageFont.truetype(font, font_size)

                width = image_data.get('width')
                height = image_data.get('height')
                margin = 20

                horizontal_top, _ = draw.textsize(top_text, font=font)
                horizontal_bottom, _ = draw.textsize(bottom_text, font=font)

                top_anchor = ((width - horizontal_top) / 2, margin)
                bottom_anchor = ((width - horizontal_bottom) / 2, height - margin - font.size)

                draw.text(top_anchor, top_text, (0, 0, 0), font=font)
                draw.text(bottom_anchor, bottom_text, (0, 0, 0), font=font)

                buffer = BytesIO()
                image.save(buffer, format="JPEG")
                image_processed = base64.b64encode(buffer.getvalue())
                image_data["base64"] = image_processed

                return image_data
