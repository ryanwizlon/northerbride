```python
from sqlalchemy import Column, Integer, String
from database import Base

class Community(Base):
    __tablename__ = 'communities'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    location = Column(String(120), unique=True)
    description = Column(String(500))

    def __init__(self, name=None, location=None, description=None):
        self.name = name
        self.location = location
        self.description = description

    def __repr__(self):
        return '<Community %r>' % (self.name)
```