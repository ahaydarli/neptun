from flask import Blueprint

dashboard_blueprint = Blueprint('dashboard_blueprint', __name__,
                                template_folder='templates')


@dashboard_blueprint.route('/')
def index():
    return {'page': 'dashboard'}
