```python
from datetime import datetime
from gallery_project.database import db

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    artwork_id = db.Column(db.Integer, db.ForeignKey('artworks.id'))
    content = db.Column(db.String(500))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, user_id, artwork_id, content):
        self.user_id = user_id
        self.artwork_id = artwork_id
        self.content = content

    def __repr__(self):
        return '<Comment {}>'.format(self.content)
```