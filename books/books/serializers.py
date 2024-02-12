from rest_framework import serializers
from .models import *



class BookSerializer(serializers.ModelSerializer):
    class Meta():
        model = Book
        fields = "__all__"

class AuthorSerializer(serializers.ModelSerializer):
    class Meta():
        model = Author
        fields = "__all__"
class WishesSerializer(serializers.ModelSerializer):
    class Meta():
        model = Wishes
        fields = "__all__"
class ArchiveSerializer(serializers.ModelSerializer):
    class Meta():
        model = Archive
        fields = "__all__"