import base64

from generator_domain.utils import font_size

from io import BytesIO

from PIL import Image, ImageFont, ImageDraw


class Generator(object):

    def __call__(self, image_data):
        self._add_text(image_data)

    def _add_text(self, image_data):
            if not image_data.get('top_text') and not image_data.get('bottom_text'):
                return image_data
            else:

                width = image_data.get('width')
                height = image_data.get('height')
                margin = 20

                font = image_data.get('font')
                image = Image.open(BytesIO(base64.b64decode(image_data.get('base64'))))
                top_text = image_data.get('top_text')
                bottom_text = image_data.get('bottom_text')
                draw = ImageDraw.Draw(image)
                _font_size = font_size(width)
                font = ImageFont.truetype(font, _font_size)

                horizontal_top, _ = draw.textsize(top_text, font=font)
                horizontal_bottom, _ = draw.textsize(bottom_text, font=font)

                top_anchor = ((width - horizontal_top) / 2, margin)
                bottom_anchor = ((width - horizontal_bottom) / 2, height - margin - font.size)

                draw.text(top_anchor, top_text, (0, 0, 0), font=font)
                draw.text(bottom_anchor, bottom_text, (0, 0, 0), font=font)

                buffer = BytesIO()
                image.save(buffer, format="JPEG")
                image_processed = base64.urlsafe_b64encode(buffer.getvalue()).decode('ascii')
                image_data["base64"] = image_processed
