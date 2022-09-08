from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Task

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

class TaskCreateForm(ModelForm):
    class Meta:
        model = Task
        exclude = ['created', 'user']