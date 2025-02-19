from django.urls import path
from . import views

urlpatterns = [
    path('brand/', views.BrandView.as_view(), name='brand'),
    path('mobile/', views.MobileView.as_view(), name='mobile'),
]
