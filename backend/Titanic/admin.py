from django.contrib import admin
from .models import Passenger, EmbarkedPlace

class EmbarkedPlaceAdmin(admin.ModelAdmin):
   list_display = (
      'Place',
   )

admin.site.register(EmbarkedPlace, EmbarkedPlaceAdmin)

class AgeListFilter(admin.SimpleListFilter):
   title = "Age"
   parameter_name = "age"

   def lookups(self, request, model_admin):
      return [
         ("18", "<= 18"),
         ("65", "> 18 and <= 65"),
         ("A", "> 65")
      ]
   
   def queryset(self, request, queryset):
      if self.value() == "18":
         return queryset.filter(Age__lte=18)
      if self.value() == "65":
         return queryset.filter(Age__gt=18, Age__lte=65)
      if self.value() == "A":
         return queryset.filter(Age__gt=65)

class PassengerAdmin(admin.ModelAdmin):
   list_display = (
      'Name',
      'Survived',
      'Gender',
      'Class',
      'Age',
      'Fare',
   )

   list_filter = (
      "Survived",
      "Gender",
      "Class",
      AgeListFilter,
      "Embarked"
   )

admin.site.register(Passenger, PassengerAdmin)