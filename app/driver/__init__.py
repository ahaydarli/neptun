from flask import Blueprint

driver_blueprint = Blueprint('driver_blueprint', __name__)

from . import views

