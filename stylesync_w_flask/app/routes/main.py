from flask import Blueprint, jsonify, request, current_app
from app import db
from app.models.user import LoginPayload
from pydantic import ValidationError
from bson import ObjectId
from app.models.products import *
from app.decorators import token_required
from datetime import datetime, timedelta, timezone
import jwt

main_bp = Blueprint('main_bp', __name__)

# FR: The system must allow a user to authenticate using a token.
# check next day
@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    try:
        raw_data = request.get_json()
        user_data = LoginPayload(**raw_data)
    except ValidationError as e:
        return jsonify({'error': e.errors()}), 400
    except Exception as e:
        return jsonify({'error': 'Error during the request'}), 500

    if user_data.username == 'admin' and user_data.password == '123':
        token = jwt.encode(
            {
                "user_id": user_data.username,
                "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
            },
            current_app.config['SECRET_KEY'],
            algorithm='HS256'
        )

        return jsonify({'access_token': token}), 200

    return jsonify({'message': 'Invalid credentials'}), 401
    

# FR: The system must allow the listing of all products.
@main_bp.route('/products', methods=['GET'])
def get_products():
    products_cursor = db.products.find({})
    products_list = [ProductDBModel(**product).model_dump(by_alias=True, exclude_none=True) for product in products_cursor]
    return jsonify(products_list)

# FR: The system must allow the creation of a new product.
@main_bp.route('/products', methods=['POST'])
@token_required
def create_product(token):
    try:
        product = Product(**request.get_json())
    except ValidationError as e:
        return jsonify({'error': e.errors()})

    result = db.products.insert_one(product.model_dump())

    return jsonify({'message': 'The product has been created',
                    'id': str(result.inserted_id)}), 201

# FR: The system must allow viewing the details of a single product.
@main_bp.route('/product/<string:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    try:
        oid = ObjectId(product_id)
    except Exception as e:
        return jsonify({'error': e})

    product = db.products.find_one({'_id':oid})

    if product:
        product_model = ProductDBModel(**product).model_dump(by_alias=True, exclude_none=True)
        return jsonify(product_model)
    else:
        return jsonify({'error': 'product not found'})
    

# FR: The system must allow the editing of a single, existing product.
@main_bp.route('/product/<int:product_id>', methods=['PUT'])
def alter_product_by_id(product_id):
    return jsonify({'message': 'Alter product route'})

# FR: The system must allow the deletion of a single, existing product.
@main_bp.route('/product/<int:product_id>', methods=['DELETE'])
def del_product_by_id(product_id):
    return jsonify({'message': 'Delete product route'})

# FR: The system must allow the import of sales via a file.
@main_bp.route('/sales/upload', methods=['POST'])
def upload_sales(sale_file):
    return jsonify({'message': 'Add sales file route'})

@main_bp.route('/')
def index():
    return jsonify({'message': 'Welcome to StyleSync!'})


