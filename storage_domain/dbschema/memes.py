from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("postgresql://postgres@localhost:5432/memegen", echo=True)
Base = declarative_base(engine)

class Memes(Base):

    __tablename__ = 'memes'

    id = Column(Integer, primary_key=True, nullable=False)
    width = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
    base64 = Column(String, nullable=False)
    mimetype = Column(String, nullable=False)
    top_text = Column(String, nullable=True)
    bottom_text = Column(String, nullable=True)
    uid = Column(String, nullable=False)
    base64_600_thumb = Column(String, nullable=True)
    base64_200_thumb = Column(String, nullable=True)

    def __init__(self, id, width, height, base64, uid,
                 mimetype, top_text=None, bottom_text=None,
                 base64_600_thumb=None, base64_200_thumb=None):

        self.id = id
        self.width = width
        self.height = height
        self.base64 = base64
        self.mimetype = mimetype
        self.top_text = top_text
        self.bottom_text = bottom_text
        self.uid = uid
        self.base64_600_thumb = base64_600_thumb
        self.base64_200_thumb = base64_200_thumb

    def serialise(self):
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "base64": self.base64,
            "mimetype": self.mimetype,
            "top_text": self.top_text,
            "bottom_text": self.bottom_text,
            "uid": self.uid,
            "base64_600_thumb": self.base64_600_thumb,
            "base64_200_thumb": self.base64_200_thumb
        }