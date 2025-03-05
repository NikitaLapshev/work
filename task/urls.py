from django.urls import path, include
from .views import TaskCreateView, TaskListView, TaskDeleteView, TaskUpdateView
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'api/tasks', TaskViewSet, basename='task')


urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('add/', TaskCreateView.as_view(), name='add_task'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='delete_task'),
    path('edit/<int:pk>/', TaskUpdateView.as_view(), name='edit_task'),
    path('api/', include(router.urls)),
]
