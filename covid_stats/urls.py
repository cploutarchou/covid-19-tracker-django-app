from django.urls import path

from . import views

urlpatterns = [
    path('maps.html', views.maps_page, name='maps')

]
