# todo/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Home page with tasks
def index(request):
    tasks = Task.objects.all()  # show all tasks publicly
    return render(request, 'todo/index.html', {'tasks': tasks})

# Add Task
def add_task(request):
    if request.method == 'POST':
        Task.objects.create(title=request.POST['title'])
    return redirect('/')

# Toggle Complete
def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('/')

# Update Task
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.save()
    return redirect('/')

# Delete Task
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('/')
