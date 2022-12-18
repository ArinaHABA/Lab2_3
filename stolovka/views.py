from django.shortcuts import render
from rest_framework import viewsets
from stolovka.models import *
from stolovka.serializers import *

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all().order_by('food_id')
    serializer_class = FoodSerializer  # Сериализатор для модели

class FoodTypeViewSet(viewsets.ModelViewSet):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer

class DormViewSet(viewsets.ModelViewSet):
    queryset = Dorm.objects.all()
    serializer_class = DormSerializer

class MenuViewSet(viewsets.ModelViewSet):
    serializer_class = FoodSerializer
    def get_queryset(self):
        return Food.objects.filter(id_food_type=self.kwargs['list_pk'])
