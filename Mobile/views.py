from django.shortcuts import render
from . models import Mobile, Brand
from .serializers import BrandSerializers, MobileSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

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
        
class MobileDetails(APIView):
    def get(self, request, pk):
        mobile = get_object_or_404(Mobile, pk=pk)
        serializer = MobileSerializers(mobile)
        return Response(serializer.data)
    
    def put(self, request, pk):
        mobile = Mobile.objects.get(pk = pk)
        serializer = MobileSerializers(mobile, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        mobile = get_object_or_404(Mobile, pk=pk)
        mobile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)