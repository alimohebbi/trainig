from django import forms

from planner.models import Muscle


class MuscleForm(forms.ModelForm):
    class Meta:
        model = Muscle
        fields = ['name']
