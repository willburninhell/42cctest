# Create your views here.
from django.shortcuts import render
from .models import Contact


def index(request):
    contact = Contact.objects.get(pk=1)
    return render(request, "core/index.html", dict(contact=contact))
