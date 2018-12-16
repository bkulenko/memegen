import base64

from io import BytesIO

from PIL import Image


class Thumbnailer(object):

    def __init__(self):
        self.thumbnail_sizes = [600, 200]

    def __call__(self, image_data):
        self._make_thumbnails(image_data)

    def _make_thumbnails(self, image_data):

        width = image_data.get("width")
        height = image_data.get("height")
        if width <= self.thumbnail_sizes[1]:
            return image_data

        base_image = base64.b64decode(image_data.get("base64"))
        base_image = Image.open(BytesIO(base_image))

        for size in self.thumbnail_sizes:
            if width > size:
                buffered_image = BytesIO()
                thumbnail_width = size
                thumbnail_height = size * (width / height)
                thumbnail_size = thumbnail_width, thumbnail_height

                base_image.thumbnail(thumbnail_size)
                base_image.save(buffered_image, format="JPEG")
                image_processed = base64.b64encode(buffered_image.getvalue())
                image_data["base64_{}_thumb".format(size)] = image_processed

                with open("test_thumbnail_{}.jpeg".format(size), "wb") as file:
                    file.write(buffered_image.getvalue())

        return image_data
