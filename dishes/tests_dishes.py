from rest_framework.test import APITestCase
from rest_framework import status


class TestDishesViews(APITestCase):

    def setUp(self):
        pass

    def test_dishes_get_list(self):
        response = self.client.post('/api/dishes/', {'title': 'new get list'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get('/api/dishes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get('/api/dishes1/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_dishes_get_detail(self):
        response = self.client.post('/api/dishes/', {'title': 'new get'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get('/api/dishes/2/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get('/api/dishes/555/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_dishes_post(self):
        response = self.client.post('/api/dishes/', {'title': 'new post'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_dishes_put(self):
        response = self.client.post('/api/dishes/', {'title': 'new put'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.put('/api/dishes/5/', {'title': 'new put test!'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get('/api/dishes/56566/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_dishes_delete(self):
        response = self.client.post('/api/dishes/', {'title': 'new delete'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.delete('/api/dishes/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get('/api/dishes/55556/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
