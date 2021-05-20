from django.shortcuts import render, get_object_or_404
from .models import Task


def home(request):
    return render(request, 'home.html')


def task_list(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'base/task_list.html', context)


def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    context = {'task': task}
    return render(request, 'base/task_detail.html', context)

