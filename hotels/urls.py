from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/hotel_list', views.hotel_list, name='hotel_list'),
    path('<int:hotel_id>/', views.hotel_detail, name='hotel_detail'),

]
