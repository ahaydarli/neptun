from flask import Blueprint

customer_blueprint = Blueprint('customer_blueprint', __name__)

from . import views

