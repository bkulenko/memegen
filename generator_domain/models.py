from base64 import b64encode
from os import urandom


class BaseImageClass(object):

    def __init__(self,
                 width=None,
                 height=None,
                 base64=None,
                 mimetype=None,
                 uid=None,):

        self.width = width
        self.height = height
        self.base64 = base64
        self.mimetype = mimetype
        self.uid = self.make_uid()

    def make_uid(self, prefix="img"):

        uid = "{}-{}".format(prefix, b64encode(urandom(9)))
        return uid


class Image(BaseImageClass):
    def __init__(self, thumbnails_uid=None, top_text=None, bottom_text=None):

        super().__init__()
        self.thumbnails_uid = thumbnails_uid


class Thumbnail(BaseImageClass):

    def __init__(self, image_uid=None):
        super().__init__()
        self.image_uid = image_uid
