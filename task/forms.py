from django.forms import ModelForm, DateInput, TextInput

from task.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'deadline']
        widgets = {
            "deadline": DateInput(attrs={"type": "date"}),
            "title": TextInput(attrs={'placeholder': "Task title"})
        }