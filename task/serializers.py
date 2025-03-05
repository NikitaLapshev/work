from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'owner', 'title', 'completed', 'deadline', 'created_at']
        read_only_fields = ['id', 'owner', 'created_at']
