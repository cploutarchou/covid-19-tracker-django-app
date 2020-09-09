import datetime
from coronavirus.common import CurrentMonth
from django.shortcuts import render

current_month = CurrentMonth()


def index(request):
    return render(request, "default/base.html", {
        'current_year': datetime.datetime.now(),
        'title': 'Home Page',
        'current_month': current_month.get_current_month(),
        'today_date': current_month.get_today_date(),
        'month_first_date': current_month.get_current_month_first_date()

    })
