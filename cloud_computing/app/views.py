from django.http import HttpResponse
from django.shortcuts import render
from .models import Food, Counter
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import FoodSerializer
from rest_framework.permissions import AllowAny


# Create your views here.
class FoodViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


def increase_counter_field(request):
    counter = Counter.objects.get_or_create(id=1)[0]
    counter.counter_field = counter.counter_field + 1
    counter.save()
    return HttpResponse(status=200)
