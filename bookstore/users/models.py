from django.db import models


class User(models.Model):
    username = models.CharField(max_length=25)
    email = models.EmailField(max_length=25)
    password = models.CharField(max_length=55)

    def __str__(self):
        return f'{self.id}: {self.username}'

