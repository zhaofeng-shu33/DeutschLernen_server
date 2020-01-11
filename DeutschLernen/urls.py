"""DeutschLernen URL Configuration
"""
from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^Word_edit/', include('Word_edit.urls')),
]
