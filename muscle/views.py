# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView

from muscle.forms import MuscleForm
from muscle.models import Muscle


class MuscleListView(generic.ListView):
    template_name = 'muscle/list.html'
    context_object_name = 'muscles'

    def get_queryset(self):
        """Return the last five published questions."""
        return Muscle.objects.order_by('-pub_date')


class MuscleView(generic.DetailView):
    model = Muscle
    template_name = 'muscle/details.html'


class MuscleCreate(CreateView):
    model = Muscle
    form_class = MuscleForm
    template_name = 'muscle/form.html'
    success_url = reverse_lazy('muscle_list')


class MuscleUpdate(UpdateView):
    model = Muscle
    template_name = 'muscle/form.html'
    form_class = MuscleForm
    success_url = reverse_lazy('muscle_list')


class MuscleDelete(DeleteView):
    model = Muscle
    context_object_name = 'exercise'
    template_name = 'muscle/delete.html'
    success_url = reverse_lazy('muscle_list')


