from .models import ToDo
from django.forms import ModelForm

class ToDoForm(ModelForm):
    class Meta:
        model = ToDo
        fields = ['name', 'memo', 'important']