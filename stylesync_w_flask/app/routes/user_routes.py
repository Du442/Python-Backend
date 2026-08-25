from crypt import methods
from bson import ObjectId
from flask import Blueprint, jsonify, request
from pydantic import ValidationError
from app import db
from user_routes import User

from stylesync_w_flask.app.decorators import token_required
from stylesync_w_flask.app.models.user import UserResponse


user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['GET'])
@token_required
def get_users(token):

    users_cursor = db.user.find({}, {"password": 0})
    users_list = []
    for user in users_cursor:
        user['_id'] = str(user['_id'])
        users_list.append(UserResponse(**user).model_dump(by_alias=True))
    return jsonify(users_list)

@user_bp.route('/users', methods=['POST'])
@token_required
def post_user(token):
    try:
        user = User(**request.get_json())
    except ValidationError as e:
        return jsonify({'error':e.errors()})
    
    result = db.user.insert_one(user.model_dump())

    return jsonify({'message': 'The user has been created',
                    'id': str(result.inserted_id)}), 201

@user_bp.route('/user/<string:user_id>', methods=['DELETE'])
@token_required
def delete_user(token, user_id):
    try:
        oid = ObjectId(user_id)
    except ValidationError as e:
        return jsonify({'error':e.errors()}), 400

    delete_data = db.user.delete_one({'_id': oid})

    if delete_data.deleted_count == 0:
        return jsonify({'message': 'user not found'}), 404

    return '', 204