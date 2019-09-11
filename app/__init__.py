from flask import Flask
from flask_debug import Debug
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()


def create_app(config_name):
    app = Flask(__name__)
    cors = CORS(app, resources={r"*": {"origins": "*"}})
    app.config.from_object(config[config_name])
    app.app_context().push()
    db.init_app(app)
    db.metadata.clear()
    db.create_all()
    ma.init_app(app)
    jwt.init_app(app)
    from .customer import customer_blueprint
    from .dashboard import dashboard_blueprint
    from .driver import driver_blueprint
    app.register_blueprint(customer_blueprint, url_prefix='/api/v1/customer')
    app.register_blueprint(dashboard_blueprint, url_prefix='/dashboard')
    app.register_blueprint(driver_blueprint, url_prefix='/api/v1/driver')

    return app


