from django.shortcuts import render
from portal.models import AMQPConnection, Automation, Run, Parameter, DaemonLog


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def automations(request):
    context = {'automations': Automation.objects.all()}
    return render(request, "automations.html", context)


def runs(request):
    pass


def daemon_logs(request):
    num_logs = 50
    context = {'logs': DaemonLog.objects.order_by('-id')[:num_logs]}
    return render(request, "daemon_logs.html", context)
