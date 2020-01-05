from django.db import models

from exercise.models import Exercise


class Workout(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    exercise_list = models.ManyToManyField(Exercise, through='WorkoutMembership')
    pub_date = models.DateField('date published')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-pub_date', 'name')


class WorkoutMembership(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    number = models.IntegerField()

    class Meta:
        ordering = ('number', )
