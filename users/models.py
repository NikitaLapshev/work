from django.db import models

class Users(models.Model):
    Username = models.CharField(max_length=160)
    Password = models.CharField(max_length=160)

    def __str__(self):
        return f'Users: {self.Username}'
