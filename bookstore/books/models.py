from django.db import models


class Book(models.Model):
    title = models.TextField(max_length=55)
    pages = models.CharField(max_length=5)
    author = models.CharField(max_length=55)
    price = models.DecimalField(max_digits=5, decimal_places=1)

    def __str__(self):
        return f'{self.id}. {self.title}'