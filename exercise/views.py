# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView

from exercise.models import Exercise


class ExerciseListView(generic.ListView):
    template_name = 'exercise/list.html'
    context_object_name = 'exercises'

    def get_queryset(self):
        """Return the last five published questions."""
        return Exercise.objects.order_by('-pub_date')


class ExerciseView(generic.DetailView):
    model = Exercise
    template_name = 'exercise/details.html'


class ExerciseCreate(CreateView):
    model = Exercise
    template_name = 'exercise/form.html'
    fields = '__all__'
    success_url = reverse_lazy('exercise_list')


class ExerciseUpdate(UpdateView):
    model = Exercise
    template_name = 'exercise/form.html'
    fields = '__all__'
    success_url = reverse_lazy('exercise_list')


class ExerciseDelete(DeleteView):
    model = Exercise
    context_object_name = 'exercise'
    template_name = 'exercise/delete.html'
    success_url = reverse_lazy('exercise_list')


