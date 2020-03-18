from rest_framework import serializers

from dishes.models import Ingredient, Dish, SIZE_CHOICES, TYPE_CHOICES


class DishSerializer(serializers.ModelSerializer):
    ingredients = serializers.PrimaryKeyRelatedField(queryset=Ingredient.objects.all(), many=True)

    class Meta:
        model = Dish
        fields = ("id", "title", "description", "size", "type", "ingredients", "created")


class IngredientSerializer(serializers.ModelSerializer):
    dishes_list = DishSerializer(many=True, read_only=True)

    class Meta:
        model = Ingredient
        fields = ("id", "title", "dishes_list", "created")

