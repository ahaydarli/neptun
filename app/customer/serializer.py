from app import ma
from .models import Customer


class CustomerSchema(ma.ModelSchema):
    class Meta:
        model = Customer


customers_schema = CustomerSchema(many=True)
