from django.db import models

from django.contrib.auth.models import User

class Food(models.Model):
    name = models.CharField(max_length=200)
    register_date = models.DateTimeField('date registered')

    energy = models.PositiveIntegerField()
    fat = models.FloatField()
    saturated_fat = models.FloatField()
    carbohydrates = models.FloatField()
    sugars = models.FloatField()
    fibers = models.FloatField()
    proteins = models.FloatField()
    salt = models.FloatField()

    quantity = models.FloatField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name