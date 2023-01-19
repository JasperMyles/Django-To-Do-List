from django import forms
from . import models

class createTodo(forms.ModelForm):
    class Meta:
        model = models.Todo
        fields = ['title', 'body']
        