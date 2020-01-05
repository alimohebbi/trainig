# Create your views here.
from django.db.models import When, Case
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView

from plan.forms import PlanForm, PlanWorkoutForm
from plan.models import Plan, PlanMembership
from workout.models import Workout


class PlanListView(generic.ListView):
    template_name = 'plan/list.html'
    context_object_name = 'plans'

    def get_queryset(self):
        return Plan.objects.all()


def count_muscle_exercise(workouts):
    primary = {}
    secondary = {}
    keys = []
    for w in workouts:
        for e in w.exercise_list.all():
            if e.primary_muscle not in primary.keys():
                primary[e.primary_muscle] = 0
            if e.secondary_muscle not in secondary.keys():
                secondary[e.secondary_muscle] = 0

            primary[e.primary_muscle] = primary[e.primary_muscle] + 1
            if e.secondary_muscle is not None:
                secondary[e.secondary_muscle] = secondary[e.secondary_muscle] + 1
    for k in primary.keys():
        if k not in secondary.keys():
            secondary[k] = 0
    for k in secondary.keys():
        if k not in primary.keys() and k is not None:
            primary[k] = 0
    results = [[k, primary[k], secondary[k]] for k in primary.keys()]

    return results


class PlanView(generic.DetailView):
    model = Plan
    template_name = 'plan/details.html'

    def get_context_data(self, **kwargs):
        context = super(PlanView, self).get_context_data(**kwargs)
        workout_ids = PlanMembership.objects.filter(plan__pk=self.object.id) \
            .order_by('number') \
            .values_list('workout', flat=True)
        preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(workout_ids)])
        workouts = Workout.objects.filter(id__in=workout_ids).order_by(preserved)
        context['workouts'] = workouts
        context['muscle_summary'] = count_muscle_exercise(workouts)
        return context


class PlanCreate(CreateView):
    object = None

    model = Plan
    template_name = 'plan/form.html'
    form_class = PlanForm
    success_url = reverse_lazy('plan_list')
    inline_fields = ['search', 'workout', 'number']

    def get(self, request, *args, **kwargs):
        self.object = None
        form = PlanForm
        ingredient_form = self.get_inline_form()
        return self.render_to_response(self.get_context_data(form=form, ingredient_form=ingredient_form))

    def get_inline_form(self):
        return inlineformset_factory(Plan, Plan.workout_list.through, fields=self.inline_fields,
                                     extra=2,
                                     form=PlanWorkoutForm)

    def post(self, request, *args, **kwargs):
        self.object = None
        ingredient_form_class = self.get_inline_form()
        ingredient_form = ingredient_form_class(self.request.POST)
        return self.evaluate_forms(ingredient_form)

    def evaluate_forms(self, ingredient_form):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
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


class PlanUpdate(UpdateView, PlanCreate):

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = PlanForm(instance=self.object)
        ingredient_form_class = self.get_inline_form()
        ingredient_form = ingredient_form_class(instance=self.object)
        return self.render_to_response(
            self.get_context_data(form=form, ingredient_form=ingredient_form))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        ingredient_form_class = self.get_inline_form()
        ingredient_form = ingredient_form_class(self.request.POST, instance=self.object)
        return self.evaluate_forms(ingredient_form)


class PlanDelete(DeleteView):
    model = Plan
    context_object_name = 'plan'
    template_name = 'plan/delete.html'
    success_url = reverse_lazy('plan_list')


def load_workouts(request):
    search = request.GET.get('search')
    workouts = Workout.objects.filter(name__contains=search).order_by('name')
    return render(request, 'exercise_dropdown_list_options.html', {'elements': workouts})
