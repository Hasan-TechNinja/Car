from django.urls import path
from . import views

urlpatterns = [
    path('', views.carlist, name='cars'),
    path('details/<int:pk>/', views.carDetails, name='details'),
    # path('details/', views.carDetails, name='details'),
    path('showroom/', views.ShowRoomView.as_view(), name='showroom'),
    path('showroom/<int:pk>', views.ShowRoomView.as_view(), name='showroom'),

]
