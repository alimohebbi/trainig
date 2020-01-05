import json

from django.http import HttpResponse
# Create your views here.
from django.views import generic

from exercise.models import Exercise
from record.models import Record


class RecordListView(generic.ListView):
    template_name = 'record/list.html'
    context_object_name = 'records'
    model = Record

    def get_context_data(self, **kwargs):
        context = super(RecordListView, self).get_context_data(**kwargs)
        records = Record.objects.all().order_by('-pub_date')[:10]
        context['dates'] = sorted(set(records.values_list('pub_date', flat=True)))
        context['exercises'] = Exercise.objects.all()
        return context


def retrieve_records(request):
    query = Record.objects.all()[:10]
    records = json.dumps(list(query.values()), sort_keys=True, default=str)
    return HttpResponse(records, content_type="application/json")


def post(request):
    value = request.POST.get('record')
    muscle = request.POST.get('exercise')
    date = request.POST.get('date')
    record = Record(muscle, value, date)
    record.save()
    print(record)
    return HttpResponse('success')


def update(request, pk):
    value = request.POST.get('record')
    muscle = request.POST.get('muscle')
    date = request.POST.get('date')
    Record.objects.filter(pk=pk).update(record=value, muscle=muscle, date=date)
    return HttpResponse('success')


def delete(request, pk):
    return None
