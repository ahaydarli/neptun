from . import dashboard_blueprint
from flask import render_template


@dashboard_blueprint.route('/')
def index():
    return render_template('index.html')
