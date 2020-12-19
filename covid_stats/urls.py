from django.urls import path, include
from covid_stats.plotly_charts import daily_growth

from . import views

urlpatterns = [
    path('maps.html', views.maps_page, name='maps'),
    path('pages/rabid_test_stats.html', views.rabid_tests_stats, name='rabid_test_stats'),
]
