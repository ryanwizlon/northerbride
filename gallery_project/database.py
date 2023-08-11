```python
from flask_sqlalchemy import SQLAlchemy
from gallery_project.config import DATABASE_URI

# Initialize SQLAlchemy with no settings
db = SQLAlchemy()

def setup_db(app):
    """
    Set up the database.
    """
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()
```