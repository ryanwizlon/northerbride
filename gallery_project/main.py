```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from gallery_project.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from gallery_project.routes import gallery, user, comment, share

if __name__ == "__main__":
    app.run(debug=True)
```