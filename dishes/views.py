from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
from dishes.serializers import DishSerializer, IngredientSerializer
from dishes.models import Ingredient, Dish, SIZE_CHOICES, TYPE_CHOICES
from rest_framework import filters


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created']
