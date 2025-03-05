from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Task(models.Model):
    owner = models.ForeignKey(User, related_name="tasks", on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=160)
    completed = models.BooleanField(default=False)
    deadline = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Task: {self.title} Deadline: {self.deadline}"


