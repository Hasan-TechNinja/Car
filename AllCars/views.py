from django.shortcuts import render
from . models import Car, ShowRoom, Bike
from . serializers import CarSerializers, ShowRoomSerializers, BikeSerializers
from django.http import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND


# Create your views here.

@api_view(['GET', 'POST'])
def carlist(request):
    if request.method == 'GET':
        cars = Car.objects.all()
        serializer = CarSerializers(cars, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = CarSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view()
def carDetails(request, pk):
    car = Car.objects.get(pk = pk)
    serializer = CarSerializers(car)
    return Response(serializer.data)


class ShowRoomView(APIView):
    def get(self, request):
        showroom = ShowRoom.objects.all()
        serializer = ShowRoomSerializers(showroom, many = True)
        return Response(serializer.data)
    
    
    def post(self, request):
        serializer = ShowRoomSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)



class ShowRoomDetailsView(APIView):
    def get(self, request, pk):
        showroom = get_object_or_404(ShowRoom, pk=pk)
        serializer = ShowRoomSerializers(showroom)
        return Response(serializer.data)
    
    def put(self, request, pk):
        showroom = ShowRoom.objects.get(pk=pk)
        serializer = ShowRoomSerializers(showroom, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        showroom = get_object_or_404(ShowRoom, pk=pk)
        showroom.delete()
        return Response({"message": "Showroom deleted successfully"}, status=HTTP_204_NO_CONTENT)

class BikeView(APIView):
    def get(self, request):
        bike = Bike.objects.all()
        serializer = BikeSerializers(bike, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BikeSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class BikeDetails(APIView):
    def get(self, request, pk):
        bike = get_object_or_404(Bike, pk=pk)
        serializer = BikeSerializers(bike)
        return Response(serializer.data)

    def put(self, request, pk):
        bike = Bike.objects.get(pk=pk)
        serializer = BikeSerializers(bike, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        bike = get_object_or_404(Bike, pk = pk)
        bike.delete()
        return Response()

# def AllCars(request):
#     cars = Car.objects.all()

#     data = {
#         'cars': list(cars.values())
#     }
#     # return render(request, 'tata.html')
#     return JsonResponse(data)

# def CarDetails(request, pk):
#     car = get_object_or_404(Car, id=pk)  # Ensures 404 response if the car does not exist
#     data = {
#         'id': car.id,
#         'name': car.name,
#         'description': car.description,
#     }
#     return JsonResponse(data)