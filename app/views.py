from django.http import HttpResponse
from django.template import loader
from django.urls import Resolver404
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from app.redis.redis_client import RedisClient
from covid_stats import data
from app.functions import Dates

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@cache_page(CACHE_TTL)
def index(request):
    redis = RedisClient(1)
    client = redis.client

    def render_view():
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

        return render(request, template_name="index.html", context=index_page_context)

    if client.get("daily_stats"):
        print("Key daily_stats exists.Start Render view.")
        return render_view()
    else:
        data.save_daily_data_to_redis()
        print("Redis key daily_stats expired.Start update key")
        return render_view()


def pages(request):
    context = {}
    try:
        load_template = request.path.split('/')[-1]
        template = loader.get_template('pages/' + load_template)
        return HttpResponse(template.render(context, request))
    except Resolver404:
        template = loader.get_template('404.html')
        return HttpResponse(template.render(context, request))
