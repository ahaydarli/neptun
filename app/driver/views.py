from . import driver_blueprint
from flask import jsonify, request
from .models.driver import Driver
from app import db
from .serializer import driver_schema, drivers_schema


@driver_blueprint.route('/')
def index():
    return jsonify({"message": "Driver index"})


@driver_blueprint.route('/registration', methods=['POST'])
def registration():
    if not request.is_json:
        return jsonify({"message": "Request is not json"})
    phone = request.json.get('phone', None)
    if not phone:
        return jsonify({"message": "Phone is missing"})
    driver = Driver(phone=phone)
    db.session.add(driver)
    db.session.commit()
    return jsonify(driver_schema.dump(driver)), 201


