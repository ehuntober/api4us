from django.test import TestCase

# Create your tests here.

from django.urls import reverse
from rest_framework import status 
from rest_framework.test import APITestCase

from books.models import Book

class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="Django for APIs",
            subtitle="Build web APiS with Python and Django",
            author = "William S. Vincent",
            isbn = "97856734955",
        )
        
    
    def test_api_listview(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(),1)
        self.assertContains(response,self.book)
        
