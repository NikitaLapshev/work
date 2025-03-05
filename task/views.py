from datetime import date
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .forms import TaskForm
from .models import Task
from django.urls import reverse_lazy
from .serializers import TaskSerializer


User = get_user_model()


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    ordering = '-id'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            "task_form": TaskForm(),
            "today": date.today()
        })
        return context

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    form_class = TaskForm
    model = Task
    success_url = reverse_lazy('task_list')




