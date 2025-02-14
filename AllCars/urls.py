from django.urls import path
from . import views

urlpatterns = [
    path('', views.carlist, name='cars'),
    path('details/<int:pk>/', views.carDetails, name='details')
    # path('details/', views.carDetails, name='details'),

]
