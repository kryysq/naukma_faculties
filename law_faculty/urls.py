from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('programs/', views.program_list_view, name='program_list'),
    path('departments/', views.department_list_view, name='department_list'),
    path('specialties/', views.specialty_list_view, name='specialty_list'),
    path('programs/<int:pk>/', views.program_detail_view, name='program_detail'),
    path('exchange-programs/', views.exchange_list_view, name='exchange_list'),
]