"""app URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from coronavirus import views

from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include

from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

# Loading plotly Dash apps script
import coronavirus.dash_daily_statistics

from django_plotly_dash.views import add_to_session

from admin_panel import views as admin_panel_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
    url('^django_plotly_dash/', include('django_plotly_dash.urls')),
    path('', TemplateView.as_view(template_name='admin_base.html'), name='home'),
    path('secure_admin/', admin_panel_views.IndexView.as_view(), name='index'),
    path('secure_admin/<int:pk>/', admin_panel_views.ContactDetailView.as_view(), name='detail'),
    path('secure_admin/edit/<int:pk>/', admin_panel_views.edit, name='edit'),
    path('secure_admin/create/', admin_panel_views.create, name='create'),
    path('secure_admints/delete/<int:pk>/', admin_panel_views.delete, name='delete')

]
urlpatterns += [
    path('secure_admin/', include('django.contrib.auth.urls')),
]
