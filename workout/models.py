from django.db import models

from exercise.models import Exercise


class Workout(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    exercise_list = models.ManyToManyField(Exercise)
    pub_date = models.DateField('date published')

    def __str__(self):
        return self.name

#
# class Plan(models.Model):
#     name = models.CharField(max_length=100)
#     pub_date = models.DateField('date published')
#     workout_list = models.ManyToManyField(Workout)
#
#     def __str__(self):
#         return self.name
