# app/tests.py

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import BookModel as Book # Убедитесь, что это правильное название вашей модели

class BookTests(APITestCase):

    def setUp(self):
        # 1. Создание тестового пользователя
        self.user = User.objects.create_user(username='testuser', password='password123')
        # 2. Аутентификация тестового клиента
        self.client.force_authenticate(user=self.user)

        # Создание тестовых данных для базы данных
        self.book_data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'price': 9.99,
            'published_date': '2024-01-01' # Добавьте дату, если это требуется моделью
        }
        self.book = Book.objects.create(**self.book_data)
        
        # Получение URL-адресов
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.pk})

    def test_list_books(self):
        """
        Проверяет, что список книг доступен по GET-запросу после аутентификации.
        """
        # Теперь запрос будет авторизован и должен вернуть 200 OK
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book')

    def test_retrieve_book(self):
        """
        Проверяет, что можно получить одну книгу по ID.
        """
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book')