from app import ma
from .models.driver import Driver


class DriverSchema(ma.ModelSchema):
    class Meta:
        model = Driver


drivers_schema = DriverSchema(many=True)
driver_schema = DriverSchema()
