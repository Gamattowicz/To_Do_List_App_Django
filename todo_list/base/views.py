from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm


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


def task_create(request):
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            title = task_form.cleaned_data['title']
            content = task_form.cleaned_data['content']
            complete = task_form.cleaned_data['complete']

            task = Task(title=title, content=content, complete=complete)
            task.save()
            request.user.task.add(task)
            return redirect('/task/')
    else:
        task_form = TaskForm()

    return render(request, 'base/task_form.html', {'task_form': task_form})


def task_update(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task_form = TaskForm(instance=task)

    return render(request, 'task_update.html', {'task_form':task_form})