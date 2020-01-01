from django import forms
from django.forms import inlineformset_factory

from exercise.models import Exercise
from muscle.models import Muscle
from workout.models import Workout


class WorkoutForm(forms.ModelForm):
    muscle = forms.ModelChoiceField(queryset=Muscle.objects.all())
    exercise_list = inlineformset_factory(Exercise, Workout, fields=('name',))

    class Meta:
        model = Workout
        fields = ['name', 'muscle', 'number', 'pub_date']
        # fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['exercise_list'].queryset = Exercise.objects.none()
        if 'muscle' in self.data:
            try:
                muscle = int(self.data.get('muscle'))
                self.fields['exercise_list'].queryset = Exercise.objects.filter(primary_muscle=muscle).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['exercise_list'].queryset = self.instance.exercise_list.order_by('name')
