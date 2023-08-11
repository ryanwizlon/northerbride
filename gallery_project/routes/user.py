```python
from flask import Blueprint, request, jsonify
from gallery_project import db
from gallery_project.models.User import User

user = Blueprint('user', __name__)

@user.route('/user', methods=['GET'])
def get_user_profile():
    user_id = request.args.get('user_id')
    user = User.query.get(user_id)
    if user:
        return jsonify(user.to_dict()), 200
    else:
        return jsonify({"message": "User not found"}), 404

@user.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

@user.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = User.query.get(user_id)
    if user:
        user.name = data['name']
        user.email = data['email']
        db.session.commit()
        return jsonify(user.to_dict()), 200
    else:
        return jsonify({"message": "User not found"}), 404

@user.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted"}), 200
    else:
        return jsonify({"message": "User not found"}), 404
```