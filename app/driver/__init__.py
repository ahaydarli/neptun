from flask import Blueprint

driver_blueprint = Blueprint('driver_blueprint', __name__)


@driver_blueprint.route('/')
def index():
    return {'page': 'driver'}
