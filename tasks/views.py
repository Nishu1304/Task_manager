# tasks/views.py

from django.shortcuts import render


def home(request):
    return render(request, 'tasks/home.html')  # Make sure the template is in the correct folder


from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# List all tasks for the logged-in user
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required  # This decorator ensures the user must be logged in to access this view
def task_list(request):
    # Check if the user is authenticated before accessing user-related data
    if request.user.is_authenticated:
        # Your logic to fetch tasks based on user.id
        tasks = Task.objects.filter(user=request.user)  # Example, assuming tasks are associated with the user
    else:
        # Handle the case where the user is not authenticated
        tasks = Task.objects.none()  # Return an empty queryset or handle accordingly

    return render(request, 'tasks/task_list.html', {'tasks': tasks})


# Create a new task
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})


# Edit an existing task
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})


# Delete a task
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')
