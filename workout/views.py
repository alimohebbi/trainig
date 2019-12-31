# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView

from workout.models import Workout


class WorkoutListView(generic.ListView):
    template_name = 'workout/list.html'
    context_object_name = 'workouts'

    def get_queryset(self):
        """Return the last five published questions."""
        return Workout.objects.order_by('-pub_date')


class WorkoutView(generic.DetailView):
    model = Workout
    template_name = 'workout/details.html'


class WorkoutCreate(CreateView):
    model = Workout
    template_name = 'workout/form.html'
    fields = '__all__'
    success_url = reverse_lazy('workout_list')


class WorkoutUpdate(UpdateView):
    model = Workout
    template_name = 'workout/form.html'
    fields = '__all__'
    success_url = reverse_lazy('workout_list')


class WorkoutDelete(DeleteView):
    model = Workout
    context_object_name = 'workout'
    template_name = 'workout/delete.html'
    success_url = reverse_lazy('workout_list')


