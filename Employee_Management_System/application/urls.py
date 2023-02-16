from django.urls import path

from . import views

urlpatterns = [
    path('',views.main, name='main'),
    path('employees/', views.employees, name='employees'),
    path('department/', views.department, name='department'),
    path('create-employees/', views.createEmployees, name='createEmployees')
]