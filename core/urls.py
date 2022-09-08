from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),

    path('addtask/', views.addTask, name='addtask'),
    path('edit-task/<int:pk>', views.editTask, name='edit-task'),
    path('delete-task/<int:pk>', views.deleteTask, name= 'delete-task'),

    path('test/', views.test, name='test'),
]