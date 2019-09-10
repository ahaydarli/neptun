from app.customer.models import Customer
from . import customer_blueprint
from .models import Customer
from .serializer import customers_schema
from flask import jsonify


@customer_blueprint.route('/')
def index():
    return {'key': 'value'}


@customer_blueprint.route('/user')
def user():
    all_customers = Customer.query.all()
    return jsonify(customers_schema.dump(all_customers))
