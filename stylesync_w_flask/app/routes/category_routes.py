from flask import Blueprint, jsonify, request
from flask.wrappers import json
from app.models.category import Category
from pydantic import ValidationError

category_bp = Blueprint('category_bp', __name__, url_prefix='/categories')

@category_bp.route('/', methods=['GET'])
def get_category():
    return jsonify({'categories': 'name'})

@category_bp.route('/', methods=['POST'])
def post_category():
    try:
        raw_data = request.get_json()
        category_data = Category(**raw_data)
    except ValidationError as e:
        return jsonify({'error': e.errors()}), 400
    except Exception as e:
        return jsonify({'error': 'Error during the request'}), 500

    return jsonify({'message': 'category registered with success!'})