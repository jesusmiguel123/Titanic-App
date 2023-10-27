from django.urls import path, include
from rest_framework import routers
from .views import PassengerViewSet

router = routers.DefaultRouter()
router.register('passenger', PassengerViewSet)

urlpatterns = [
   path('', include(router.urls)),
   path('auth/', include('rest_framework.urls', namespace='rest_framework_titanic'))
]