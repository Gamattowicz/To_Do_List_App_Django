from django import forms
from .models import Task, Category
from django.forms.widgets import TextInput


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'content', 'complete']
        title = forms.CharField(label='Title', max_length=200)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'color']
        widgets = {
            'color': TextInput(attrs={'type': 'color'})
        }