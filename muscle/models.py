from django.db import models


class Muscle(models.Model):
    name = models.CharField(max_length=100)
    pub_date = models.DateField('date published')

    def __str__(self):
        return self.name


