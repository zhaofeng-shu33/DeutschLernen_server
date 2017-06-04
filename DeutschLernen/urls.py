"""DeutschLernen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from . import views
from .views import WordList
urlpatterns = [
    url(r'^admin/', admin.site.urls),#administrator login
    url(r'^$', views.index, name='index'),
    url(r'^(?P<root_page_name>[a-z_]+\.html)$',views.root_page_request,name='root_page_request'),
    url(r'^Word_edit/', include('Word_edit.urls')),
    url(r'^Word_test/',include('Word_test.urls')),
    url(r'^corpus_service/',include('corpus_service.urls')),
    url(r'^(?P<xml_file>[NAV][0-9]+\.xml)$',views.wordxml,name='wordxml'),
    url(r'^wordlist/$',WordList.as_view()),
    #create a new submodule called wordedit
]
