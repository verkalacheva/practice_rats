from django.urls import reverse
from rest_framework import status
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from books.models import Book, Author, Wishes, Archive
from django.contrib.auth.models import User



class TestViews(APITestCase):

    def setUp(self):
        # Создаем юзеров
        self.user1 = User.objects.create(username='testuser1')
        self.user2 = User.objects.create(username='testuser2')
        self.user3 = User.objects.create(username='testuser3')


        # Создаем авторов
        self.author1 = Author.objects.create(name='Test Author1')
        self.author2 = Author.objects.create(name='Test Author2')
        self.author3 = Author.objects.create(name='Test Author3')

        # создаем книги
        self.book1 = Book.objects.create(name='Test Book1', id_author=self.author1)
        self.book2 = Book.objects.create(name='Test Book2', id_author=self.author2)
        self.book3 = Book.objects.create(name='Test Book3', id_author=self.author3)
        

        # создаем виши
        self.wish1 = Wishes.objects.create(id_user=self.user1.pk, id_book=self.book1)
        self.wish2 = Wishes.objects.create(id_user=self.user1.pk, id_book=self.book2)
        self.wish3 = Wishes.objects.create(id_user=self.user2.pk, id_book=self.book3)


        # создаем архивы
        self.arch1 = Archive.objects.create(id_user=self.user2.pk, id_book=self.book1)
        self.arch2 = Archive.objects.create(id_user=self.user2.pk, id_book=self.book2)
        self.arch3 = Archive.objects.create(id_user=self.user3.pk, id_book=self.book3)

    # вывод всех авторов (эндпоинт all-authors)
    def test_author_list(self):
        response = self.client.get(reverse('all-authors'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Author.objects.count())

    # успешное добавление автора (эндпоинт add-author)
    def test_author_add_success(self):
        authors_len = Author.objects.count()

        data = {'name': 'Alexander Pushkin'}
        response = self.client.post(reverse('add-author'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), authors_len + 1)
    
    # неуспешная попытка добавить автора (с пустым именем)
    def test_author_add_failure(self):
        authors_len = Author.objects.count()

        data = {'name': ''}
        response = self.client.post(reverse('add-author'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Author.objects.count(), authors_len)

    # вывод всех книг (эндпоинт all-books)
    def test_book_list(self):
        response = self.client.get(reverse('all-books'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Book.objects.count())

    # получить книгу по id (эндпоинт books-by-id)
    def test_book_by_id(self):
        response = self.client.get(reverse('books-by-id', kwargs={'id': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 'Test Book1')
    
    # получить книгу по не существующему id
    def test_non_existant_book_by_id(self):
        response = self.client.get(reverse('books-by-id', kwargs={'id': 42}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # успешное добавление книги
    def test_book_add_success(self):
        books_len = Book.objects.count()

        data = {'name': 'Test Book4', 'id_author': self.author1.pk}
        response = self.client.post(reverse('add-book'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), books_len + 1)

    # неуспешное добавление книги(без автора)
    def test_book_add_failure(self):
        books_len = Book.objects.count()

        data = {'name': 'Test Book5'}
        response = self.client.post(reverse('add-book'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Book.objects.count(), books_len)

    # успешное получение книги по автору
    def test_book_by_author_success(self):
        response = self.client.get(reverse('books-by-author', kwargs={'author_id': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 'Test Book1')
        

    # неуспешное полеучение книги по автору
    def test_book_by_author_failure(self):
        response = self.client.get(reverse('books-by-author', kwargs={'author_id': 10}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)









    


    
