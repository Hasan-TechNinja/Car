from django.urls import path
from . import views

urlpatterns = [
    path('brand/', views.BrandView.as_view(), name='brand'),
    path('mobile/', views.MobileView.as_view(), name='mobile'),
    path('mobiledetails/<int:pk>', views.MobileDetails.as_view(), name='mobile'),
    path('review/', views.ReviewView.as_view(), name='review')
]
