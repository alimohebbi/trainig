from django.db import models

# Create your models here.

from django.db import models

from exercise.models import Exercise


class Record(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='exercise')
    value = models.FloatField()
    pub_date = models.DateField('date published')

    def __init__(self, exercise, value, pub_date, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.exercise = Exercise.objects.get(pk=exercise)
        self.value = value
        self.pub_date = pub_date

    def __str__(self):
        return self.exercise.name

    class Meta:
        ordering = ['pub_date', ]
