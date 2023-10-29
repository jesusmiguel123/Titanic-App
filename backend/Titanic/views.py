from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action

from .models import Passenger, EmbarkedPlace
from .serializers import (
   EmbarkedPlaceSerializer,
   PassengerSerializer,
   PredictPassengerSerializer
)
from .apps import TitanicConfig

class CustomPagination(PageNumberPagination):
   page_size = 10
   page_size_query_param = 'limit'

   def get_paginated_response(self, data):
      return Response({
         'totalPages': self.page.paginator.num_pages,
         'count': self.page.paginator.count,
         'previous': self.get_previous_link(),
         'next': self.get_next_link(),
         'results': data
      })

class EmbarkedPlaceViewSet(ModelViewSet):
   queryset = EmbarkedPlace.objects.all()
   serializer_class = EmbarkedPlaceSerializer

   def create(self, request):
      data = request.data
      many = isinstance(data, list)
      serializer = self.get_serializer(data=data, many=many)
      if serializer.is_valid():
         self.perform_create(serializer)
         return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
         )
      return Response(
         serializer.errors,
         status=status.HTTP_400_BAD_REQUEST
      )

class PassengerViewSet(ModelViewSet):
   queryset = Passenger.objects.all()
   serializer_class = PassengerSerializer
   pagination_class = CustomPagination

   def create(self, request):
      data = request.data
      many = isinstance(data, list)
      serializer = self.get_serializer(data=data, many=many)
      if serializer.is_valid():
         self.perform_create(serializer)
         return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
         )
      return Response(
         serializer.errors,
         status=status.HTTP_400_BAD_REQUEST
      )
   
   @action(
      detail=False,
      methods=["GET", "POST"],
      serializer_class=PredictPassengerSerializer
   )
   def predict(self, request):
      data = request.data
      serializer = self.get_serializer(data=data)
      if serializer.is_valid():
         gender_to_number = {
            "male": 0.0,
            "female": 1.0
         }

         embarked_to_number = {
            "Cherbourg": 0.0,
            "Queenstown": 1.0,
            "Southampton": 2.0
         }

         features = {
            "Class": None,
            "Gender": gender_to_number[data.get("Gender")],
            "Age": None,
            "SibSp": None,
            "ParCh": None,
            "Fare": None,
            "Embarked": embarked_to_number[data.get("Embarked")]
         }

         for feature in features:
            if features[feature] == None:
               features[feature] = float(data.get(feature))

         features_values = [list(features.values())]

         Survived = TitanicConfig.model.predict(features_values)

         return Response({
            "Survived": True if Survived == 1 else False
         }, status=status.HTTP_200_OK)
      return Response(
         serializer.errors,
         status=status.HTTP_400_BAD_REQUEST
      )