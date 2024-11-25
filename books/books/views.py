from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .serializers import *
from .models import *
from django.db import transaction
from models import Offer



class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request, *args, **kwargs):
        data = list(Book.objects.all().values())
        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        data = list(Book.objects.filter(pk=kwargs['id']).values())
        return Response(data)

    def create(self, request, *args, **kwargs):
        product_serializer_data = BookSerializer(data=request.data)
        if product_serializer_data.is_valid():
            product_serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Book Added Sucessfully"}, status = status_code)
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "please fill the datails"},status = status_code)


    def get_by_author(self, request, *args, **kwargs):
        data = list(Book.objects.filter(id_author=kwargs['author_id']).values())
        return Response(data)



class AuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def list(self, request, *args, **kwargs):
        data = list(Author.objects.all().values())
        return Response(data)

    def create(self, request, *args, **kwargs):
        product_serializer_data = AuthorSerializer(data=request.data)
        if product_serializer_data.is_valid():
            product_serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Author Added Sucessfully"}, status=status_code)
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "please fill the datails"}, status=status_code)


class WishesView(viewsets.ModelViewSet):
    queryset = Wishes.objects.all()
    serializer_class = WishesSerializer

    def list(self, request, *args, **kwargs):
        data = list(Wishes.objects.all().values())
        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        data = list(Wishes.objects.filter(id_user=kwargs['id_user']).values())
        return Response(data)

    def create(self, request, *args, **kwargs):
        product_serializer_data = WishesSerializer(data=request.data)
        if product_serializer_data.is_valid():
            product_serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Wish Added Sucessfully"}, status = status_code)
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "please fill the datails"}, status = status_code)

    def destroy(self, request, *args, **kwargs):
        product_data = Wishes.objects.filter(id_user=kwargs['id_user']).filter(id_book=kwargs['id_book'])
        if product_data:
            product_data.delete()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Wish deleted Sucessfully"}, status = status_code)
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Product data not found"}, status = status_code)
    def match(self, request, *args, **kwargs):
        wishes_data = list(Wishes.objects.filter(id_user=kwargs['id_wants']).values_list('id_book', flat=True))
        if not wishes_data:
            return Response([])
        book_list = []
        for i in wishes_data:

            archive_data = list(Archive.objects.filter(id_book=i).values())
            for j in archive_data:
                book_list.append(j)
        return Response(book_list)


class ArchiveView(viewsets.ModelViewSet):
    queryset = Archive.objects.all()
    serializer_class = ArchiveSerializer

    def list(self, request, *args, **kwargs):
        data = list(Archive.objects.all().values())
        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        data = list(Archive.objects.filter(id_user=kwargs['id_user']).values())
        return Response(data)

    def create(self, request, *args, **kwargs):
        product_serializer_data = ArchiveSerializer(data=request.data)
        if product_serializer_data.is_valid():
            product_serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Book Added Sucessfully to Archive"}, status = status_code)
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "please fill the datails"}, status = status_code)

    def destroy(self, request, *args, **kwargs):
        product_data = Archive.objects.filter(id_user=kwargs['id_user']).filter(id_book=kwargs['id_book'])
        if product_data:
            product_data.delete()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Archive deleted Sucessfully"}, status = status_code)
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Product data not found"}, status = status_code)