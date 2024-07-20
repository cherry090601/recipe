from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    preparation_time = models.IntegerField()
    ingredients = models.TextField()
    steps = models.TextField()

    def __str__(self):
        return self.name
