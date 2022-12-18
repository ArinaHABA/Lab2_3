from stolovka.models import *
from rest_framework import serializers


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model=Food
        # Поля, которые мы сериализуем
        fields=["food_id", "id_food_type", "food_name", "food_price", "weight", "is_in_stock", "image"]

class FoodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=FoodType
        fields=["type_id", "type_name"]

class DormSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dorm
        fields=["dorm_id", "dorm_address"]