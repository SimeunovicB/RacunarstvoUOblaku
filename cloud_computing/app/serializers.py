from rest_framework.serializers import ModelSerializer
from .models import Food, Counter


class FoodSerializer(ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'name', 'rating', 'date_made', 'healthy']


class CounterSerializer(ModelSerializer):
    class Meta:
        model = Counter
        fields = ['id', 'counter_field']
