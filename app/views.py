from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.urls import Resolver404

from covid_stats import data
from app.functions import Dates

cases = data.daily_new_cases()
daily_tests = data.daily_tests_performed()
daily_deaths = data.daily_deaths()
rate = data.new_cases_rate_compared_yesterday_date()
today_date = Dates.get_today_date()
index_page_context = {
    "date": today_date,
    "new_cases": {"title": "Today Cases", "cases": cases},
    "daily_test": {"title": "Today Tests", "test": daily_tests},
    "daily_deaths": {"title": "Today Deaths", "deaths": daily_deaths},
    "rate": {"title": "Today Rate", "rate": rate},
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
    except Resolver404:
        template = loader.get_template('404.html')
        return HttpResponse(template.render(context, request))
