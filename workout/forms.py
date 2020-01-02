from django import forms
from djangoformsetjs.utils import formset_media_js

from exercise.models import Exercise
from muscle.models import Muscle
from workout.models import Workout, WorkoutMembership


class WorkoutExerciseForm(forms.ModelForm):
    muscle = forms.ModelChoiceField(queryset=Muscle.objects.all(),
                                    widget=forms.Select(attrs={'class': 'muscle_select', }))

    class Meta:
        model = WorkoutMembership
        fields = ['muscle', 'exercise', 'number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if hasattr(self, 'cleaned_data'):
            try:
                if 'muscle' in self.cleaned_data.keys():
                    muscle = self.cleaned_data['muscle']
                    self.fields['exercise'].queryset = Exercise.objects.filter(primary_muscle=muscle).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['exercise'].queryset = Exercise.objects.all()
            # self.fields['exercise'].queryset = Exercise.objects.filter(
            #     primary_muscle=self.instance.exercise.primary_muscle).order_by('name')
            self.fields['muscle'].initial = self.instance.exercise.primary_muscle


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'number', 'pub_date']

    class Media(object):
        js = formset_media_js
