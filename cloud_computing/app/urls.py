from django.urls import path, include
from rest_framework import routers
from .views import FoodViewSet, increase_counter_field

router = routers.DefaultRouter()

router.register(r'foods', FoodViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('counter/', increase_counter_field),
]