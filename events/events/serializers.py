from rest_framework import serializers
from .models import *



class EventsSerializer(serializers.ModelSerializer):
    class Meta():
        model = Events
        fields = "__all__"