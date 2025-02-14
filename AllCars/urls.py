from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllCars, name='tata'),
    path('details/', views.CarDetails, name='details'),
    path('details/<int:pk>/', views.CarDetails, name='details')

]
