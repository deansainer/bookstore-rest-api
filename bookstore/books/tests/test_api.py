from rest_framework import APITestCase, status
from django.urls import reverse
from books.models import Book




class BookApiTestCase(APITestCase):
    def test_create_book(self):
        url = reverse('book-list')
        data = {'title': 'Hamlet'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, 'Hamlet')