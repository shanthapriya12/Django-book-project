from django.test import TestCase
from .models import Book


class BookModelTest(TestCase):

    def test_book_creation(self):

        book = Book.objects.create(
            title='Python Basics',
            author='John',
            price=250
        )

        self.assertEqual(
            book.title,
            'Python Basics'
        )