from django.shortcuts import render
from .models import Task


def home(request):
    return render(request, 'home.html')


def task_list(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'base/task_list.html', context)


