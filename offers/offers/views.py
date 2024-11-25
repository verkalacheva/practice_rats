from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import *
from .serializers import*


class OfferView(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

    def list(self, request, *args, **kwargs):
        data = list(Offer.objects.all().values())
        return Response(data)

    def retrieve_from(self, request, *args, **kwargs):
        data_from = list(Offer.objects.filter(id=kwargs['id_from']).values())
        return Response(data_from)

    def retrieve_to(self, request, *args, **kwargs):
        data_to = list(Offer.objects.filter(id=kwargs['id_to']).values())
        return Response(data_to)

    def retrieve_status(self, request, *args, **kwargs):
        data_book = list(Offer.objects.filter(id=kwargs['id_status']).values())
        return Response(data_book)


    def create(self, request, *args, **kwargs):
        product_serializer_data = OfferSerializer(data=request.data)
        if product_serializer_data.is_valid():
            product_serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Offer Added Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "please fill the datails", "status": status_code})

    def destroy(self, request, *args, **kwargs):
        product_data = Offer.objects.filter(id=kwargs['pk'])
        if product_data:
            product_data.delete()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Offer delete Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Offer data not found", "status": status_code})

