```python
from flask import Blueprint, render_template, request
from gallery_project.models.Artwork import Artwork
from gallery_project.models.Community import Community
from gallery_project.utils import loadGallery

gallery = Blueprint('gallery', __name__)

@gallery.route('/gallery', methods=['GET'])
def get_gallery():
    communities = Community.query.all()
    artworks = []
    for community in communities:
        community_artworks = Artwork.query.filter_by(community_id=community.id).all()
        artworks.extend(community_artworks)
    return render_template('gallery.html', artworks=artworks)

@gallery.route('/gallery', methods=['POST'])
def post_gallery():
    data = request.get_json()
    community_name = data.get('community_name')
    community = Community.query.filter_by(name=community_name).first()
    if not community:
        return {"message": "Community not found"}, 404
    artwork = Artwork(
        title=data.get('title'),
        description=data.get('description'),
        image_url=data.get('image_url'),
        community_id=community.id
    )
    db.session.add(artwork)
    db.session.commit()
    loadGallery()
    return {"message": "Artwork added successfully"}, 201
```