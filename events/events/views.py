from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .serializers import *
from .models import *
# Create your views here.


class EventView(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

    def list(self, request, *args, **kwargs):
        data = list(Events.objects.all().values())
        return Response(data)

    def get_by_user(self, request, *args, **kwargs):
        data = list(Events.objects.filter(id_user=kwargs['id_user']).values())
        return Response(data)

    def get_by_id(self, request, *args, **kwargs):
        data = list(Events.objects.filter(id=kwargs['id']).values())
        return Response(data)

    def get_by_id_status(self, request, *args, **kwargs):
        data = list(Events.objects.filter(id_status=kwargs['id_status']).values())
        return Response(data)

    def create(self, request, *args, **kwargs):
        product_serializer_data = EventsSerializer(data=request.data)
        if product_serializer_data.is_valid():
            product_serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Event Added Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "please fill the datails", "status": status_code})

    def destroy(self, request, *args, **kwargs):
        product_data = Events.objects.filter(id=kwargs['id'])
        if product_data:
            product_data.delete()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Wish deleted Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Product data not found", "status": status_code})

