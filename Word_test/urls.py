app_name='Word_test'
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^test_config$', views.test_config_response,),
]
