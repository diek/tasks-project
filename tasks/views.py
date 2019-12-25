from django.shortcuts import render


def reporting(request):
    reports = {
        'COM': 'Comms',
        'TP': 'Team Player',
        'TL': 'Team Leader',
        'TB': 'Toxic Behavior',
        'AVT': 'Abusive Verbal/Text'
    }
    return render(request, 'tasks/reporting.html', {'reports': reports})
