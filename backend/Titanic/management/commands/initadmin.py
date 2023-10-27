from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from dotenv import load_dotenv
import os

load_dotenv()

class Command(BaseCommand):
   def handle(self, *args, **options):
      if User.objects.count() == 0:
         user = User.objects.create(
            username=os.environ.get('ADMIN_USER'),
            email=os.environ.get('ADMIN_EMAIL'),
            is_staff=True,
            is_superuser=True
         )
         user.set_password(os.environ.get('ADMIN_PASSWORD'))
         user.save()
         self.stdout.write(self.style.SUCCESS('Successfully created initial admin user'))
      else:
         self.stdout.write(self.style.SUCCESS('An admin user already exists'))