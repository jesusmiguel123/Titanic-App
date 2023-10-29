from django.core.management.base import BaseCommand
from Titanic.models import EmbarkedPlace, Passenger
from pathlib import Path
from json import loads

class Command(BaseCommand):
   def handle(self, *args, **options):
      print("Embarked Places Table:")
      places = ["Cherbourg", "Southampton", "Queenstown"]
      if EmbarkedPlace.objects.count() == 0:
         for i, place in enumerate(places):
            ep = EmbarkedPlace.objects.create(Place=place)
            ep.save()
            print(
               f"\r   Populating embarked places... {i+1}/{len(places)}",
               end=""
            )
         self.stdout.write(
            self.style.SUCCESS("\n   Embarked Places populated!")
         )
      else:
         self.stdout.write(
            self.style.SUCCESS("   Embarked Places already populated!")
         )

      print("Passengers Table:")

      BASE_DIR = Path(__file__).resolve().parent.parent.parent

      passengers = None

      with open(BASE_DIR / "data" / "passengers.json") as f:
         passengers = loads(f.read())
      
      passengers = passengers[:100]

      if Passenger.objects.count() == 0:
         for i, passenger in enumerate(passengers):
            ep = EmbarkedPlace.objects.get(
               Place=passenger["Embarked"]
            )
            new_passenger = Passenger.objects.create(
               Survived=passenger["Survived"],
               Class=passenger["Class"],
               Name=passenger["Name"],
               Gender=passenger["Gender"],
               Age=passenger["Age"],
               SibSp=passenger["SibSp"],
               ParCh=passenger["ParCh"],
               Fare=passenger["Fare"],
               Embarked=ep
            )
            new_passenger.save()
            print(
               f"\r   Populating passengers... {i+1}/{len(passengers)}",
               end=""
            )
         self.stdout.write(
            self.style.SUCCESS("\n   Passengers populated!")
         )
      else:
         self.stdout.write(
            self.style.SUCCESS("   Passengers already populated!")
         )
      self.stdout.write(
         self.style.SUCCESS('DB populated!')
      )