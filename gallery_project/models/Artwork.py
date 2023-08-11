```python
from sqlalchemy import Column, Integer, String, Text
from database import Base

class Artwork(Base):
    __tablename__ = 'artworks'

    id = Column(Integer, primary_key=True)
    artwork_name = Column(String(100), unique=True)
    community_name = Column(String(100))
    description = Column(Text)
    image_url = Column(String(500))
    short_story = Column(Text)
    joke = Column(Text)

    def __init__(self, artwork_name=None, community_name=None, description=None, image_url=None, short_story=None, joke=None):
        self.artwork_name = artwork_name
        self.community_name = community_name
        self.description = description
        self.image_url = image_url
        self.short_story = short_story
        self.joke = joke

    def __repr__(self):
        return '<Artwork %r>' % (self.artwork_name)
```