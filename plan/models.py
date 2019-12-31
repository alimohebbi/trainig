from django.db import models

from workout.models import Workout


class Plan(models.Model):
    name = models.CharField(max_length=100)
    pub_date = models.DateField('date published')
    workout_list = models.ManyToManyField(Workout)

    def __str__(self):
        return self.name
