from django.db import models

# Create your models here.


class Author(models.Model): # all Authors
    name = models.CharField(max_length=255)


class Book(models.Model): # all books in/. our database
    name = models.CharField(max_length=255)
    id_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    #photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    #objects = models.Manager()

class Archive(models.Model):
    id_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    
    class Meta:
        verbose_name = 'Архив'
        verbose_name_plural = 'Архив'

    def __str__(self):
        return f'{self.id_book.name} на полке у пользователя  {self.id_user}(хочет отдать)'

class Wishes(models.Model):
    id_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    
    class Meta:
        verbose_name = 'Желание'
        verbose_name_plural = 'Желания'

    def __str__(self):
        return f'{self.id_book.name} желание пользователя {self.id_user}'




