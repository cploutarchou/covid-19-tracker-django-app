# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from covid_stats import data

cases = data.daily_new_cases()
index_page_context = {
    "new_cases": {"title": "Today Cases", "cases": cases},
    "dashboard_text": "Daily Statistics"
}


def index(request):
    return render(request, template_name="index.html", context=index_page_context)


def pages(request):
    context = {}
    try:
        load_template = request.path.split('/')[-1]
        template = loader.get_template('pages/' + load_template)
        return HttpResponse(template.render(context, request))
    except:
        template = loader.get_template('404.html')
        return HttpResponse(template.render(context, request))
