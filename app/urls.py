from django.contrib import admin
from django.urls import path, include
from app import views

from django.contrib import admin
from django.conf.urls import url,re_path
from django.urls import path, include

from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

# Loading plotly Dash apps script
import covid_stats.plotly_charts.daily_growth

from django_plotly_dash.views import add_to_session

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    re_path(r'^.*\.html', views.pages, name='pages'),

    # The home page
    path('', views.index, name='home'),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
    url('^django_plotly_dash/', include('django_plotly_dash.urls')),
]
