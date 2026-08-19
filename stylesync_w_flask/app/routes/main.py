from flask import Blueprint, jsonify, request
from app import db
from app.models.user import LoginPayload
from pydantic import ValidationError
from bson import ObjectId

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
        return jsonify({'message': 'Sucessfully login'})
    else:
        return jsonify({'message': 'Invalid credentials'})
    

# FR: The system must allow the listing of all products.
@main_bp.route('/products', methods=['GET'])
def get_products():
    products_cursor = db.products.find({})
    products_list = []
    for products in products_cursor:
        products['_id'] = str(products['_id'])
        products_list.append(products)

    return jsonify(products_list)

# FR: The system must allow the creation of a new product.
@main_bp.route('/products', methods=['POST'])
def create_product():
    return jsonify({'message': 'Create products route'})

# FR: The system must allow viewing the details of a single product.
@main_bp.route('/product/<string:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    try:
        oid = ObjectId(product_id)
    except Exception as e:
        return jsonify({'error': e})

    product = db.products.find_one({'_id':oid})

    if product:
        product['_id'] = str(product['_id'])
        return jsonify(product)
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


