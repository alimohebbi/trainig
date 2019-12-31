from django.db import models

# Create your models here.
from muscle.models import Muscle


class Exercise(models.Model):
    primary_muscle = models.ForeignKey(Muscle, on_delete=models.CASCADE, related_name='primary_muscle')
    secondary_muscle = models.ForeignKey(Muscle, on_delete=models.CASCADE, related_name='secondary_muscle', blank=True,
                                         null=True)
    name = models.CharField(max_length=100)
    pub_date = models.DateField('date published')
    tutorial_link = models.CharField(max_length=1000, blank=True)
    comment = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.name

#
# class Workout(models.Model):
#     number = models.IntegerField()
#     name = models.CharField(max_length=100)
#     exercise_list = models.ManyToManyField(Exercise)
#     pub_date = models.DateField('date published')
#
#     def __str__(self):
#         return self.name
#
#
# class Plan(models.Model):
#     name = models.CharField(max_length=100)
#     pub_date = models.DateField('date published')
#     workout_list = models.ManyToManyField(Workout)
#
#     def __str__(self):
#         return self.name
