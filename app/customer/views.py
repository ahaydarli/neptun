from . import customer_blueprint
from .models.customer import Customer
from .serializer import customers_schema, customer_schema
from flask import jsonify, request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from app import db
from .controllers.users import *


@customer_blueprint.route('/')
def index():
    return {'key': 'value'}


@customer_blueprint.route('/users')
def user():
    users = get_all_users()
    return jsonify(customers_schema.dump(users)), 200


@customer_blueprint.route('/registration', methods=['POST'])
def registration():
    if not request.is_json:
        return jsonify({'message': "Request is not json"}), 400
    phone = request.json.get('phone', None)
    if not phone:
        return jsonify({"message": "Missing phone parameter"}), 400
    customer = Customer(phone=phone)
    db.session.add(customer)
    db.session.commit()
    return jsonify(customer_schema.dump(customer)), 200


@customer_blueprint.route('login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({'message': "Request is not json"}), 400
    phone = request.json.get('phone', None)
    if not phone:
        return jsonify({"message": "Missing phone parameter"}), 400
    customer = Customer.query.filter_by(phone=phone).first()
    if not customer:
        return jsonify({"message": "User not found"})
    access_token = create_access_token(identity=customer.phone)
    return jsonify(access_token=access_token), 200


@customer_blueprint.route('/logout')
def logout():
    pass


@customer_blueprint.route('/me')
@jwt_required
def me():
    current_user = get_jwt_identity()
    return jsonify(logged_user=current_user), 200


