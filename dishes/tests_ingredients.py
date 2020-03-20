from rest_framework.test import APITestCase
from rest_framework import status


class TestIngredientsViews(APITestCase):

    def setUp(self):
        pass

    def test_ingredients_get_list(self):
        response = self.client.post('/api/ingredients/', {'title': 'new get list'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get('/api/ingredients/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get('/api/ingredients1/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_ingredients_get_detail(self):
        response = self.client.post('/api/ingredients/', {'title': 'new get detail'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get('/api/ingredients/2/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get('/api/ingredients/555/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_ingredients_post(self):
        response = self.client.post('/api/ingredients/', {'title': 'new post'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_ingredients_put(self):
        response = self.client.post('/api/ingredients/', {'title': 'new put'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.put('/api/ingredients/5/', {'title': 'new put!!!'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.put('/api/ingredients/666/', {'title': 'new title'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_ingredients_delete(self):
        response = self.client.post('/api/ingredients/', {'title': 'new delete'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.delete('/api/ingredients/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.delete('/api/ingredients/777/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
