# Create your views here.
from django.shortcuts import render
from .models import Contact, RequestLog


def index(request):
    contact = Contact.objects.get(pk=1)
    return render(request, "core/index.html", dict(contact=contact))


def requests(request):
    entries = RequestLog.objects.all()[:10]
    return render(request, "core/requests.html", {'entries': entries})
