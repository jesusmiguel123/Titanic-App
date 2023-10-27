from rest_framework.serializers import (
   ModelSerializer,
   ReadOnlyField
)
from .models import Passenger

class PassengerSerializer(ModelSerializer):
   class Meta:
      model = Passenger
      fields = '__all__'

class PredictPassengerSerializer(ModelSerializer):
   Survived = ReadOnlyField()
   class Meta:
      model = Passenger
      fields = '__all__'