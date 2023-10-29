from rest_framework.serializers import (
   ModelSerializer,
   ReadOnlyField
)
from .models import Passenger, EmbarkedPlace

class EmbarkedPlaceSerializer(ModelSerializer):
   class Meta:
      model = EmbarkedPlace
      fields = '__all__'

class PassengerSerializer(ModelSerializer):
   class Meta:
      model = Passenger
      fields = '__all__'

class PredictPassengerSerializer(ModelSerializer):
   Survived = ReadOnlyField()
   class Meta:
      model = Passenger
      fields = '__all__'