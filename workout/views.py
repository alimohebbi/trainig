# Create your views here.
from django.db.models import Case, When
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView

from exercise.models import Exercise
from workout.forms import WorkoutForm, WorkoutExerciseForm
from workout.models import Workout, WorkoutMembership


class WorkoutListView(generic.ListView):
    template_name = 'workout/list.html'
    context_object_name = 'workouts'

    def get_queryset(self):
        """Return the last five published questions."""
        return Workout.objects.order_by('-pub_date')


class WorkoutView(generic.DetailView):
    model = Workout
    template_name = 'workout/details.html'

    def get_context_data(self, **kwargs):
        context = super(WorkoutView, self).get_context_data(**kwargs)
        exercise_ids= WorkoutMembership.objects.filter(workout__pk=self.object.id) \
            .order_by('number') \
            .values_list('exercise', flat=True)
        preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(exercise_ids)])
        context['exercises'] = Exercise.objects.filter(id__in=exercise_ids).order_by(preserved).values()
        return context


class WorkoutCreate(CreateView):
    model = Workout
    template_name = 'workout/form.html'
    form_class = WorkoutForm
    success_url = reverse_lazy('workout_list')

    def get(self, request, *args, **kwargs):
        self.object = None
        form = WorkoutForm
        fields = ['muscle', 'exercise', 'number']
        ingredient_form = inlineformset_factory(Workout, Workout.exercise_list.through, fields=fields, extra=2,
                                                form=WorkoutExerciseForm)
        return self.render_to_response(self.get_context_data(form=form, ingredient_form=ingredient_form))

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        fields = ['muscle', 'exercise', 'number']
        ingredient_form_class = inlineformset_factory(Workout, Workout.exercise_list.through, fields=fields, extra=2,
                                                      form=WorkoutExerciseForm)
        ingredient_form = ingredient_form_class(self.request.POST)
        if form.is_valid() and ingredient_form.is_valid():
            return self.form_valid(form, ingredient_form)
        else:
            return self.form_invalid(form, ingredient_form)

    def form_valid(self, form, ingredient_form):
        self.object = form.save()
        ingredient_form.instance = self.object
        ingredient_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, ingredient_form):
        return self.render_to_response(
            self.get_context_data(form=form,
                                  ingredient_form=ingredient_form))


class WorkoutUpdate(UpdateView, WorkoutCreate):

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = WorkoutForm(instance=self.object)
        fields = ['muscle', 'exercise', 'number']
        ingredient_form = inlineformset_factory(Workout, Workout.exercise_list.through, fields=fields, extra=2,
                                                form=WorkoutExerciseForm)
        return self.render_to_response(
            self.get_context_data(form=form, ingredient_form=ingredient_form(instance=self.object)))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        fields = ['muscle', 'exercise', 'number']
        ingredient_form_class = inlineformset_factory(Workout, Workout.exercise_list.through, fields=fields, extra=2,
                                                      form=WorkoutExerciseForm)
        ingredient_form = ingredient_form_class(self.request.POST, instance=self.object)
        if form.is_valid() and ingredient_form.is_valid():
            return self.form_valid(form, ingredient_form)
        else:
            return self.form_invalid(form, ingredient_form)


#
# class WorkoutUpdate(UpdateView):
#     model = Workout
#     template_name = 'workout/form.html'
#     form_class = WorkoutForm
#     success_url = reverse_lazy('workout_list')
#

class WorkoutDelete(DeleteView):
    model = Workout
    context_object_name = 'workout'
    template_name = 'workout/delete.html'
    success_url = reverse_lazy('workout_list')


def load_exercises(request):
    muscle = request.GET.get('muscle')
    print(muscle)
    exercises = Exercise.objects.filter(primary_muscle=muscle).order_by('name')
    print(exercises)
    return render(request, 'workout/exercise_dropdown_list_options.html', {'exercises': exercises})
