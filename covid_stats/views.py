from django.shortcuts import render

from . import maps


def maps_page(request):
    plot_div = maps.cyprus_map()
    return render(request, template_name='pages/maps.html', context={'cyprus_map': plot_div})


def rabid_tests_stats(request):
    index_page_context = {}
    return render(request, template_name="pages/rabid_test_stats.html", context=index_page_context)
