"""DeutschLernen URL Configuration
"""
from django.conf.urls import include,url
from django.contrib import admin
from . import views
from .views import WordList
urlpatterns = [
    url(r'^admin/', admin.site.urls),#administrator login
    url(r'^$', views.index, name='index'),
    url(r'^(?P<wordform>[A-Za-z]+)\.html$', views.wordhtml, name='wordhtml'),
    url(r'^Word_edit/', include('Word_edit.urls')),
    url(r'^Word_test/',include('Word_test.urls')),
#    url(r'^corpus_service/',include('corpus_service.urls')),
    # N3.xml, A4.xml etc.
    url(r'^(?P<wordform>[A-Za-z]+)\.xml$', views.wordxml, name='wordxml'),
    url(r'^wordlist/$',WordList.as_view()),
    #create a new submodule called wordedit
]
