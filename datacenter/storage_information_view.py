from datacenter.models import Visit
from datacenter.models import format_duration
from django.shortcuts import render

def storage_information_view(request):
    non_closed_visits = [{
        "who_entered":visit.passcard,
        "entered_at": visit.entered_at,
        "duration": format_duration(visit.get_duration()),
        "is_strange": visit.is_visit_long()
    }for visit in Visit.objects.filter(leaved_at=None)]

    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
