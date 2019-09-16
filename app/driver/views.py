from . import driver_blueprint
from flask import jsonify, request
from .models.driver import Driver
from .models.driver_sms import DriverSms
from app import db
from .serializer import driver_schema, drivers_schema
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity, get_raw_jwt
from ..common.helpers.sms_provider import *

@driver_blueprint.route('/')
def index():
    return jsonify({"message": "Driver index"})


@driver_blueprint.route('/registration', methods=['POST'])
def registration():
    if not request.is_json:
        return jsonify({
            "message": "Request is not json"
        })
    phone = request.json.get('phone', None)
    if not phone:
        return jsonify({"message": "Phone is missing"})
    code = generate_code()
    message = send_sms(phone, code)
    if message.status == 'accepted':
        sms = DriverSms(phone=phone, code=code)
        db.session.add(sms)
        db.session.commit()
    else:
        return jsonify({"message": "Couldn't send sms. Try again"})
    driver = Driver(phone=phone)
    db.session.add(driver)
    db.session.commit()
    return jsonify(driver_schema.dump(driver)), 201


@driver_blueprint.route('/sms-verification', methods=['POST'])
def verify_sms():
    if not request.is_json:
        return jsonify({
            "message": "Request is not json"
        })
    phone = request.json.get('phone', None)
    code = request.json.get('code', None)
    if not phone:
        return jsonify({"message": "Phone is missing"})
    if not code:
        return jsonify({"message": "Code is missing"})
    sms = DriverSms.query.filter_by(phone=phone, code=code).first()
    if sms:
        driver = Driver.query.filter_by(phone=phone).first()
        driver.status = 1
        db.session.commit()
        access_token = create_access_token(identity=driver.phone)
        db.session.delete(sms)
        db.session.commit()
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Not found"}), 400


@driver_blueprint.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({'message': "Request is not json"}), 400
    phone = request.json.get('phone', None)
    if not phone:
        return jsonify({"message": "Missing phone parameter"}), 400
    driver = Driver.query.filter_by(phone=phone).first()
    if not driver:
        return jsonify({"message": "Driver not found"})
    access_token = create_access_token(identity=driver.phone)
    return jsonify(access_token=access_token), 200


@driver_blueprint.route('/logout')
@jwt_required
def logout():
    jti = get_raw_jwt()['jti']
    #add token to blacklist and revoke
    return jsonify({"msg": "Successfully logged out"}), 200


