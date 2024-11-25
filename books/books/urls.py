from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('books/list', BookView.as_view({'get': 'list'}), name='all-books'),
    path('books/get/<int:id>/', BookView.as_view({'get': 'retrieve'}), name='books-by-id'),
    path('books/get_by_author/<int:author_id>/', BookView.as_view({'get': 'get_by_author'}), name='books-by-author'),
    path('books/add', BookView.as_view({'post': 'create'}), name='add-book'),
    path('author/list', AuthorView.as_view({'get': 'list'}), name='all-authors'),
    path('author/add', AuthorView.as_view({'post': 'create'}), name='add-author'),
    path('wishes/list', WishesView.as_view({'get': 'list'}), name='all-wishes'),
    path('wishes/get/<int:id_user>', WishesView.as_view({'get': 'retrieve'}), name='wishes-by-user'),
    path('wishes/add', WishesView.as_view({'post': 'create'}), name='add-wish'),
    path('wishes/delete/<int:id_book>/<int:id_user>', WishesView.as_view({'delete': 'destroy'}), name='delete-wish'),
    path('archive/list', ArchiveView.as_view({'get': 'list'}), name='all-archive'),
    path('archive/get/<int:id_user>', ArchiveView.as_view({'get': 'retrieve'}), name='archive-by-id'),
    path('archive/add', ArchiveView.as_view({'post': 'create'}), name='add'),
    path('archive/delete/<int:id_book>/<int:id_user>', ArchiveView.as_view({'delete': 'destroy'}), name='all-bo'),
    path('wishes/match/<int:id_wants>/', WishesView.as_view({'get' : 'match'}), name='matching'),

]