from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from django.utils import timezone
from django.views import generic

from planner.forms import MuscleForm
from planner.models import Muscle


def muscle_list(request):
    muscles = Muscle.objects.order_by('pub_date')
    context = {
        'muscles': muscles,
    }
    return render(request, 'planner/muscle_list.html', context)


def muscle_new(request):
    if request.method == "POST":
        form = MuscleForm(request.POST)
        if form.is_valid():
            muscle = form.save(commit=False)
            muscle.pub_date = timezone.now()
            muscle.save()
        return redirect('muscle_detail', pk=muscle.pk)
    else:
        form = MuscleForm()
    return render(request, 'planner/muscle_edit.html', {'form': form})


def muscle_edit(request, pk):
    muscle = get_object_or_404(Muscle, pk=pk)
    if request.method == "POST":
        form = MuscleForm(request.POST, instance=muscle)
        if form.is_valid():
            muscle = form.save(commit=False)
            muscle.pub_date = timezone.now()
            muscle.save()
            return redirect('muscle_detail', pk=muscle.pk)
    else:
        form = MuscleForm(instance=muscle)
    return render(request, 'planner/muscle_edit.html', {'form': form})



class MuscleListView(generic.ListView):
    template_name = 'planner/muscle_list.html'
    context_object_name = 'muscles'

    def get_queryset(self):
        """Return the last five published questions."""
        return Muscle.objects.order_by('-pub_date')


class MuscleView(generic.DetailView):
    model = Muscle
    template_name = 'planner/muscle_detail.html'
