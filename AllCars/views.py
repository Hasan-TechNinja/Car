from django.shortcuts import render
from . models import Car
from django.http import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404


# Create your views here.

def AllCars(request):
    cars = Car.objects.all()

    data = {
        'cars': list(cars.values())
    }
    # return render(request, 'tata.html')
    return JsonResponse(data)

def CarDetails(request, pk):
    car = get_object_or_404(Car, id=pk)  # Ensures 404 response if the car does not exist
    data = {
        'id': car.id,
        'name': car.name,
        'description': car.description,
    }
    return JsonResponse(data)