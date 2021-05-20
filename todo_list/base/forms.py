from django import forms


class TaskForm(forms.Form):
    title = forms.CharField(label='Title', max_length=200)
    content = forms.CharField(label='Description', widget=forms.Textarea)
    complete = forms.BooleanField(label='Complete')