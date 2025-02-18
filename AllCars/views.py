from django.shortcuts import render
from . models import Car, ShowRoom
from . serializers import CarSerializers, ShowRoomSerializers
from django.http import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView


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