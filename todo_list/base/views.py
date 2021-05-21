from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.list import ListView


class TaskLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('base:tasks')


def home(request):
    return render(request, 'home.html')


class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'


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
            return reverse('/task/')
    else:
        task_form = TaskForm()

    return render(request, 'base/task_form.html', {'task_form': task_form})


def task_update(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task_form = TaskForm(instance=task)
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            title = task_form.cleaned_data['title']
            content = task_form.cleaned_data['content']
            complete = task_form.cleaned_data['complete']
            task.title = title
            task.content = content
            task.complete = complete
            task.save()
            return redirect('/task/')
    return render(request, 'task_update.html', {'task_form':task_form})


def task_delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('/task/')
    return render(request, 'task_delete.html', {'task':task})