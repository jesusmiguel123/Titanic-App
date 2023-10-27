from django.contrib import admin
from .models import Passenger

class PassengerAdmin(admin.ModelAdmin):
   list_display = (
      'Name',
      'Survived',
      'Gender',
      'Class',
      'Age',
      'Fare',
   )

admin.site.register(Passenger, PassengerAdmin)