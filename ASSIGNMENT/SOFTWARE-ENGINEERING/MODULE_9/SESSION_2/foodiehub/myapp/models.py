from django.db import models


class Resturant(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    rating = models.IntegerField()

    def __str__(self):
        return self.name