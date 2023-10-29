from django.urls import path, include
from rest_framework import routers
from .views import PassengerViewSet, EmbarkedPlaceViewSet

router = routers.DefaultRouter()
router.register('passenger', PassengerViewSet)
router.register('embarked-place', EmbarkedPlaceViewSet)

urlpatterns = [
   path('', include(router.urls)),
   path('auth/', include('rest_framework.urls', namespace='rest_framework_titanic'))
]