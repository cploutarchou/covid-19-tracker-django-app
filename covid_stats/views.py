from django.shortcuts import render

from . import maps, data


def index(request):
    return render(request, template_name='index.html')


def maps_page(request):
    plot_div = maps.cyprus_map()
    return render(request, template_name='pages/maps.html', context={'cyprus_map': plot_div})


def new_cases(request):
    cases = data.daily_new_cases()
    _data = {"title": "Today Cases", "cases": cases}
    return render(request=request, template_name="cards/new_cases.html", context=_data)
