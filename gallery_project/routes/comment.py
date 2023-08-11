```python
from flask import Blueprint, request, jsonify
from gallery_project import db
from gallery_project.models.Comment import Comment
from gallery_project.models.Artwork import Artwork
from gallery_project.models.User import User

comment = Blueprint('comment', __name__)

@comment.route('/comment', methods=['POST'])
def post_comment():
    data = request.get_json()
    user_id = data.get('user_id')
    artwork_id = data.get('artwork_id')
    content = data.get('content')

    user = User.query.get(user_id)
    artwork = Artwork.query.get(artwork_id)

    if not user or not artwork:
        return jsonify({'message': 'User or Artwork not found'}), 404

    new_comment = Comment(content=content, user_id=user_id, artwork_id=artwork_id)
    db.session.add(new_comment)
    db.session.commit()

    return jsonify({'message': 'comment-posted', 'comment': new_comment.to_dict()}), 201

@comment.route('/comment/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    comment = Comment.query.get(comment_id)

    if not comment:
        return jsonify({'message': 'Comment not found'}), 404

    db.session.delete(comment)
    db.session.commit()

    return jsonify({'message': 'Comment deleted'}), 200
```