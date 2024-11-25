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
        self.user1 = User.objects.create(username='user1')
        self.user2 = User.objects.create(username='user2')
        self.user3 = User.objects.create(username='user3')


        # Создаем авторов
        self.author1 = Author.objects.create(name='Test Author1')
        self.author2 = Author.objects.create(name='Test Author2')
        self.author3 = Author.objects.create(name='Test Author3')

        # создаем книги
        self.book1 = Book.objects.create(name='Test Book1', id_author=self.author1)
        self.book2 = Book.objects.create(name='Test Book2', id_author=self.author2)
        self.book3 = Book.objects.create(name='Test Book3', id_author=self.author3)
        self.book4 = Book.objects.create(name='Test Book4', id_author=self.author1)
        
        # Создаем пожелания для пользователя 1
        self.wishes1 = [
            Wishes.objects.create(id_user=self.user1.pk, id_book=self.book1),
            Wishes.objects.create(id_user=self.user1.pk, id_book=self.book2),
            Wishes.objects.create(id_user=self.user1.pk, id_book=self.book3),
        ]
        
        # Создаем пожелания для пользователя 2
        self.wishes2 = [
            Wishes.objects.create(id_user=self.user2.pk, id_book=self.book2),
            Wishes.objects.create(id_user=self.user2.pk, id_book=self.book3),
            Wishes.objects.create(id_user=self.user2.pk, id_book=self.book4),
        ]
        # Создаем пожелания для пользователя 3
        self.wishes3 = [
            Wishes.objects.create(id_user=self.user3.pk, id_book=self.book2),
            Wishes.objects.create(id_user=self.user3.pk, id_book=self.book3),
        ]
        
        # Создаем архив для пользователя 1
        Archive.objects.create(id_user=self.user1.pk, id_book=self.book4)
        
        # Создаем архив для пользователя 2
        Archive.objects.create(id_user=self.user2.pk, id_book=self.book1)

        # Создаем архив для пользователя 3
        Archive.objects.create(id_user=self.user3.pk, id_book=self.book1)

        # Создаем нового пользователя без архива и вишлиста
        self.user4 = User.objects.create(username='user4')

    # вывод всех авторов (эндпоинт all-authors)
    # def test_author_list(self):
    #     response = self.client.get(reverse('all-authors'))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data), Author.objects.count())

    # # успешное добавление автора (эндпоинт add-author)
    # def test_author_add_success(self):
    #     authors_len = Author.objects.count()

    #     data = {'name': 'Alexander Pushkin'}
    #     response = self.client.post(reverse('add-author'), data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Author.objects.count(), authors_len + 1)
    
    # # неуспешная попытка добавить автора (с пустым именем)
    # def test_author_add_failure(self):
    #     authors_len = Author.objects.count()

    #     data = {'name': ''}
    #     response = self.client.post(reverse('add-author'), data)
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertEqual(Author.objects.count(), authors_len)

    # # вывод всех книг (эндпоинт all-books)
    # def test_book_list(self):
    #     response = self.client.get(reverse('all-books'))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data), Book.objects.count())

    # # получить книгу по id (эндпоинт books-by-id)
    # def test_book_by_id(self):
    #     response = self.client.get(reverse('books-by-id', kwargs={'id': 1}))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data[0]['name'], 'Test Book1')
    
    # # получить книгу по не существующему id
    # def test_non_existant_book_by_id(self):
    #     response = self.client.get(reverse('books-by-id', kwargs={'id': 42}))
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # # успешное добавление книги
    # def test_book_add_success(self):
    #     books_len = Book.objects.count()

    #     data = {'name': 'Test Book4', 'id_author': self.author1.pk}
    #     response = self.client.post(reverse('add-book'), data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Book.objects.count(), books_len + 1)

    # # неуспешное добавление книги(без автора)
    # def test_book_add_failure(self):
    #     books_len = Book.objects.count()

    #     data = {'name': 'Test Book5'}
    #     response = self.client.post(reverse('add-book'), data)
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertEqual(Book.objects.count(), books_len)

    # # успешное получение книги по автору
    # def test_book_by_author_success(self):
    #     response = self.client.get(reverse('books-by-author', kwargs={'author_id': 1}))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data[0]['name'], 'Test Book1')
        
    # # неуспешное полеучение книги по автору
    # def test_book_by_author_failure(self):
    #     response = self.client.get(reverse('books-by-author', kwargs={'author_id': 10}))
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_match_function(self):
        # Тестируем функцию match для виша пользователя 1
        response = self.client.get(reverse('matching', kwargs={'id_wants': self.user1.pk}))
        expected_books = [(1, 2), (1, 3)]  # Книги из виша пользователя 1
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(set([(item['id_book_id'], item['id_user']) for item in response.data]), set(expected_books))

        # Тестируем функцию match для виша пользователя 2
        response = self.client.get(reverse('matching', kwargs={'id_wants': self.user2.pk}))
        
        expected_books = [(4, 1)]  # Книги из архива пользователя 2 и виша пользователя 1
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(set([(item['id_book_id'], item['id_user']) for item in response.data]), set(expected_books))

    def test_match_with_no_matches(self):
        # Тестируем случай, когда нет совпадений (виш пользователя 3)
        response = self.client.get(reverse('matching', kwargs={'id_wants': self.user3.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual([item['id_book_id'] for item in response.data], [])

    def test_match_with_no_wishes(self):
        # Проверяем, что функция вернет пустой список(пользователь 4 без виша)
        response = self.client.get(reverse('matching', kwargs={'id_wants': self.user4.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual([item['id_book_id'] for item in response.data], [])
    

    # вывод всех записей в архивах (эндпоинт all-archive)
    def test_archive_list(self):
        response = self.client.get(reverse('all-archive'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Archive.objects.count())

    # вывод всех записей в желаниях (эндпоинт all-wishes)
    def test_wishes_list(self):
        response = self.client.get(reverse('all-wishes'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Wishes.objects.count())

    # получить список желаний по id (эндпоинт wishes-by-user)
    def test_wishes_by_id(self):
        response = self.client.get(reverse('wishes-by-user', kwargs={'id': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
    
    # получить список архивированного по id (эндпоинт archive-by-id)
    def test_archive_by_id(self):
        response = self.client.get(reverse('archive-by-id', kwargs={'id': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    

    
    


    










    


    
