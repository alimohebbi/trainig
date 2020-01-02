from django import forms
from djangoformsetjs.utils import formset_media_js

from plan.models import Plan
from workout.models import Workout, WorkoutMembership


class PlanWorkoutForm(forms.ModelForm):
    search = forms.CharField(max_length=200,
                             widget=forms.TextInput(attrs={'class': 'workout_search ', 'type': 'text'}), required=False)

    class Meta:
        model = WorkoutMembership
        fields = ['search', 'workout', 'number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if hasattr(self, 'cleaned_data'):
            try:
                if 'search' in self.cleaned_data.keys():
                    search = self.cleaned_data['search']
                    self.fields['workout'].queryset = Workout.objects.filter(name__contains=search).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['workout'].queryset = Workout.objects.all()


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['name', 'pub_date']

    class Media(object):
        js = formset_media_js
