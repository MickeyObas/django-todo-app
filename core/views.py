from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages

from .models import Task
from .forms import TaskCreateForm, MyUserCreationForm

from .decorators import already_logged_in


@already_logged_in
# Prevents an already logged-in user from attempting to register 
def register(request):

    form = MyUserCreationForm()

    if request.method == 'POST':
        print("Submitting?")
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = new_user.username.lower()
            new_user.save()
            return redirect('login')
        else:
            return render(request, 'core/register.html', {"form": form})

    return render(request, "core/register.html", {"form":form})

@already_logged_in
# Prevents an already logged in user from attempting to login again
def login(request):

    if request.method =='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(request, email=email, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials!')
            return redirect('login')

    return render(request, 'core/login.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    tasks = Task.objects.filter(user=request.user)

    return render(request, "core/home.html", {"tasks":tasks})


@login_required(login_url='login')
def addTask(request):
    form = TaskCreateForm()

    if request.method == 'POST':
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('home')
        else:
            return redirect('addTask')
    return render(request, 'core/addtask.html', {"form": form})


@login_required(login_url='login')
def editTask(request, pk):
    task = get_object_or_404(Task, id=pk)
    form = TaskCreateForm(instance=task)

    if request.method == 'POST':
        form = TaskCreateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages.error(request, "Whoops")
            return redirect('edit-task', pk=pk)

    return render(request, 'core/editTask.html', {"form":form})


@login_required(login_url='login')
def deleteTask(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == 'POST':
        task = get_object_or_404(Task, id=pk)
        task.delete()
        return redirect('home')

    return render(request, 'core/delete.html', {"task": task})


def test(request):
    return render(request, 'core/test.html')