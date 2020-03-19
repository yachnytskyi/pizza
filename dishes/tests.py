from django.test import TestCase
from dishes.models import Dish, Ingredient


class TestModels(TestCase):

    def setUp(self):
        Ingredient.objects.create(title="Ingredient 1")
        Ingredient.objects.create(title="Ingredient 2")
        Ingredient.objects.create(title="Ingredient 3")
        Dish.objects.create(title="Dish 1")
        Dish.objects.create(title="Dish 2")
        Dish.objects.create(title="Dish 3")

    def test_ingredient_is_assigned_title_on_creation(self):
        ingredient1 = Ingredient.objects.get(title="Ingredient 1")
        self.assertEquals(ingredient1.title, 'Ingredient 1')

    def test_dish_is_assigned_title_on_creation(self):
        dish1 = Dish.objects.get(title="Dish 1")
        self.assertEquals(dish1.title, 'Dish 1')

    def test_dish_is_assigned_ingredient_title_on_creation(self):
        dish1 = Dish.objects.get(title="Dish 1")
        ingredient1 = Ingredient.objects.get(title="Ingredient 1")
        dish1.ingredients.add(ingredient1)
        self.assertEquals(list(dish1.ingredients.all()), [ingredient1])

    def test_dish_is_assigned_ingredients_titles_on_creation(self):
        dish2 = Dish.objects.get(title="Dish 2")
        ingredient1 = Ingredient.objects.get(title="Ingredient 1")
        ingredient2 = Ingredient.objects.get(title="Ingredient 2")
        ingredient3 = Ingredient.objects.get(title="Ingredient 3")
        dish2.ingredients.add(ingredient1, ingredient2, ingredient3)
        self.assertEquals(list(dish2.ingredients.all()), [ingredient1, ingredient2, ingredient3])

    def test_ingredient_is_assigned_dish_title_on_creation(self):
        ingredient1 = Ingredient.objects.get(title="Ingredient 1")
        dish1 = Dish.objects.get(title="Dish 1")
        ingredient1.dishes_list.add(dish1)
        self.assertEquals(list(ingredient1.dishes_list.all()), [dish1])

    def test_ingredient_is_assigned_dishes_titles_on_creation(self):
        ingredient2 = Ingredient.objects.get(title="Ingredient 2")
        dish1 = Dish.objects.get(title="Dish 1")
        dish2 = Dish.objects.get(title="Dish 2")
        dish3 = Dish.objects.get(title="Dish 3")
        ingredient2.dishes_list.add(dish1, dish2, dish3)
        self.assertEquals(list(ingredient2.dishes_list.all()), [dish1, dish2, dish3])


