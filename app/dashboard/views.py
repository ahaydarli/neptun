from . import dashboard_blueprint
from flask import render_template
from ..driver.models.driver import Driver
from ..customer.models.customer import Customer


@dashboard_blueprint.route('/')
def index():
    return render_template('index.html')


@dashboard_blueprint.route('/driver-index')
def driver_index():
    drivers = Driver.query.all()
    return render_template('driver-index.html', drivers=drivers)


@dashboard_blueprint.route('/customer-index')
def customer_index():
    customers = Customer.query.all()
    return render_template('customer-index.html', customers=customers)
