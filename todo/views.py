# todo/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Task

# Home page with tasks
@login_required
def index(request):
    tasks = Task.objects.filter(user=request.user)  # only current user's tasks
    return render(request, 'todo/index.html', {'tasks': tasks})

# Add Task
@login_required
def add_task(request):
    if request.method == 'POST':
        Task.objects.create(user=request.user, title=request.POST['title'])
    return redirect('/')

# Toggle Complete
@login_required
def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('/')

# Update Task
@login_required
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.save()
    return redirect('/')

# Delete Task
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('/')

# User Registration
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('/')
    return render(request, 'todo/register.html')

# User Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'todo/login.html')

# User Logout
def logout_view(request):
    logout(request)
    return redirect('/login/')
