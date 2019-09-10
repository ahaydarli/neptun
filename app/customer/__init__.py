from flask import Blueprint

customer_blueprint = Blueprint('customer_blueprint', __name__)

@customer_blueprint.route('/')
def index():
    return {'page': 'customer_index'}
