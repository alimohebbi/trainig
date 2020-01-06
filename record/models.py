from django.db import models

# Create your models here.

from django.db import models

from exercise.models import Exercise


class Record(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='exercise')
    value = models.FloatField()
    pub_date = models.DateField('date published')


    def __str__(self):
        return self.exercise.name

    class Meta:
        ordering = ['pub_date', ]
