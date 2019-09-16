from twilio.rest import Client
from flask import session
import random


# def send_confirmation_code(to_number):
#     verification_code = generate_code()
#     send_sms(to_number, verification_code)
#     session['verification_code'] = verification_code
#     return verification_code


def generate_code():
    return str(random.randrange(100000, 999999))


def send_sms(to_number, body):
    account_sid = ''
    auth_token = ''
    messaging_service_sid = ''
    client = Client(account_sid, auth_token)
    message = client.api.messages.create(to_number, messaging_service_sid=messaging_service_sid, body=body)
    return message

