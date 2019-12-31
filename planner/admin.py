from django.contrib import admin

# Register your models here.
from planner.models import Exercise, Plan, Workout, Muscle

admin.site.register(Exercise)
admin.site.register(Plan)
admin.site.register(Workout)
admin.site.register(Muscle)
