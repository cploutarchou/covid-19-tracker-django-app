import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path


def index(request):
    return render(request, "default/base.html", {
        'current_year': datetime.datetime.now(),
        'title': 'Home Page'
    })

