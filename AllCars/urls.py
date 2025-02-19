from django.urls import path
from . import views

urlpatterns = [
    path('', views.carlist, name='cars'),
    path('details/<int:pk>/', views.carDetails, name='details'),
    # path('details/', views.carDetails, name='details'),
    path('showroom/', views.ShowRoomView.as_view(), name='showroom'),
    path('showroom/<int:pk>', views.ShowRoomView.as_view(), name='showroom'),
    path('roomdetails/<int:pk>/', views.ShowRoomDetailsView.as_view(), name='room-details'),
    path('bike/', views.BikeView.as_view(), name='bike'),
    path('bikeDetails/<int:pk>', views.BikeDetails.as_view(), name='bike'),

]
