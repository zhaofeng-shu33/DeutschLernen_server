from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create_new_word$', views.create_response, name='create_new_word'),
]
