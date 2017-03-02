from django.http import HttpResponse
from django.contrib.staticfiles import finders

def index(request):
    return HttpResponse('<script>window.location="static/index.html"</script>')
    #page redirection to index.html
