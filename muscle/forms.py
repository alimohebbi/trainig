from django import forms

from muscle.models import Muscle


class MuscleForm(forms.ModelForm):
    class Meta:
        model = Muscle
        fields = '__all__'
