from django.test import TestCase
from dishes.models import Dish, Ingredient


class TestModels(TestCase):

    def setUp(self):
        self.ingredient1 = Ingredient.objects.create(
            title='Ingredient 1'
        )
        self.ingredient2 = Ingredient.objects.create(
            title='Ingredient 2'
        )

    def test_ingredient_is_assigned_title_on_creation(self):
        self.assertEquals(self.ingredient1.title, 'Ingredient 1')

    def test_dish_is_assigned_title_on_creation(self):
        self.dish1 = Dish.objects.create(
            title="Dish 1"
        )
        self.assertEquals(self.dish1.title, 'Dish 1')

    def test_dish_is_assigned_ingredient_title_on_creation(self):
        self.dish1 = Dish.objects.create(
            title="Dish 1"
        )
        self.dish1.ingredients.add(self.ingredient1)
        self.assertEquals(list(self.dish1.ingredients.all()), [self.ingredient1])

