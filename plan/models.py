from django.db import models

from workout.models import Workout


class Plan(models.Model):
    name = models.CharField(max_length=100)
    pub_date = models.DateField('date published')
    workout_list = models.ManyToManyField(Workout, through='PlanMembership')

    def __str__(self):
        return self.name


class PlanMembership(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    number = models.IntegerField()

    class Meta:
        ordering = ('number',)
