from django import forms
from django.forms import ModelForm
from .models import *


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add tasks'}))

    class Meta:
        model = Task
        fields = '__all__'

    widgets = {
        'title': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Add tasks"
        }),
        'status': forms.CheckboxInput(attrs={
            'class': 'form-check-input',
            'role': "switch"
        })
    }