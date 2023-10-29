from django.db import models
from django.core.validators import (
   MinValueValidator,
   MaxValueValidator,
   DecimalValidator
)

class EmbarkedPlace(models.Model):   
   Place = models.CharField(
      max_length=20,
      unique=True,
      null=False
   )

   def __str__(self):
      return self.Place

class Passenger(models.Model):
   class ClassChoices(models.IntegerChoices):
      FIRST_CLASS = 1
      SECOND_CLASS = 2
      THIRD_CLASS = 3
   
   class GenderChoices(models.TextChoices):
      MALE = "male"
      FEMALE = "female"
   
   age_validator = MaxValueValidator(
      100,
      "Age must be >= 0 and <= 100"
   )
   sibsp_validator = MaxValueValidator(
      10,
      "Quantity of siblings plus spouses must be >= 0 and <= 10"
   )
   parch_validator = MaxValueValidator(
      10,
      "Quantity of parents plus children must be >= 0 and <= 10"
   )
   fare_validators = [
      MinValueValidator(
         0.0,
         "Fare must be >= 0"
      ),
      MaxValueValidator(
         600.0,
         "Fare must be <= 600"
      )
   ]

   Survived = models.BooleanField(
      default=False
   )
   Class = models.PositiveSmallIntegerField(
      choices=ClassChoices.choices
   )
   Name = models.CharField(
      max_length=100,
      null=False
   )
   Gender = models.CharField(
      max_length=6,
      choices=GenderChoices.choices
   )
   Age = models.PositiveSmallIntegerField(
      validators=[age_validator],
      null=False      
   )
   SibSp = models.PositiveSmallIntegerField(
      validators=[sibsp_validator],
      null=False
   )
   ParCh = models.PositiveSmallIntegerField(
      validators=[parch_validator],
      null=False
   )
   Fare = models.FloatField(
      validators=fare_validators,
      null=False
   )
   Embarked = models.ForeignKey(
      EmbarkedPlace,
      on_delete=models.CASCADE,
      to_field='Place'
   )

   def __str__(self):
      return self.Name