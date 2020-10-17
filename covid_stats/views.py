from django.shortcuts import render

from . import maps


def index(request):
    return render(request, template_name='index.html')


def maps_page(request):
    plot_div = maps.cyprus_map()
    return render(request, template_name='pages/maps.html', context={'cyprus_map': plot_div})
