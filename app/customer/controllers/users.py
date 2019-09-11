from flask import jsonify
from ..models.customer import Customer
from ..serializer import customers_schema


def get_all_users():
    all_customers = Customer.query.all()
    return all_customers
