from django.shortcuts import render
from portal.models import AMQPConnection, Automation, Parameter


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def automations(request):
    context = {'automations': Automation.objects.all()}
    return render(request, "automations.html", context)


def runs(request):
    pass
