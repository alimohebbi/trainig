# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView

from plan.models import Plan


class PlanListView(generic.ListView):
    template_name = 'plan/list.html'
    context_object_name = 'plans'

    def get_queryset(self):
        """Return the last five published questions."""
        return Plan.objects.order_by('-pub_date')


class PlanView(generic.DetailView):
    model = Plan
    template_name = 'plan/details.html'


class PlanCreate(CreateView):
    model = Plan
    template_name = 'plan/form.html'
    fields = '__all__'
    success_url = reverse_lazy('plan_list')


class PlanUpdate(UpdateView):
    model = Plan
    template_name = 'plan/form.html'
    fields = '__all__'
    success_url = reverse_lazy('plan_list')


class PlanDelete(DeleteView):
    model = Plan
    context_object_name = 'plan'
    template_name = 'plan/delete.html'
    success_url = reverse_lazy('plan_list')


