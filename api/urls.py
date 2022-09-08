from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.apihome, name='apihome'),
    path('task/<str:pk>', views.getTask, name='get-task'),
    path('add/', views.addTask, name='add'),  
]