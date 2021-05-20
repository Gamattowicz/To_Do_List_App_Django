from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'content', 'complete']
        title = forms.CharField(label='Title', max_length=200)