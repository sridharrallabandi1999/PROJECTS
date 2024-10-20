from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    stock = models.PositiveIntegerField(default=1)
    added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
