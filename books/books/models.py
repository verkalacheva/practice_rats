from django.db import models

# Create your models here.


class Author(models.Model): # all Authors
    name = models.CharField(max_length=255)


class Book(models.Model): # all books in/. our database
    name = models.CharField(max_length=255)
    id_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    #photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    #objects = models.Manager()

class Wishes(models.Model): # books that user wants
    id_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    id_user = models.IntegerField()

class Archive(models.Model): # books that user has
    id_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    id_user = models.IntegerField()


