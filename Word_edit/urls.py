from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create_new_word$', views.create_response, name='create_response'),
    #learn xss basic
    url(r'^xss', views.query_response),
    url(r'^manage_articles$',views.manage_articles),
]
