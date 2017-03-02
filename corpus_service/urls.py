app_name='corpus_service'
from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^example_search.*', views.example_response,),
]
