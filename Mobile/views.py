from django.shortcuts import render
from . models import Mobile, Brand
from .serializers import BrandSerializers, MobileSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class BrandView(APIView):
    def get(self, request):
        brand = Brand.objects.all()
        serializer = BrandSerializers(brand, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BrandSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class MobileView(APIView):
    def get(self, request):
        mobile = Mobile.objects.all()
        serializer = MobileSerializers(mobile, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MobileSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)