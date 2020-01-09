from django.http import HttpResponse
def index(request):
    '''page redirection to index.html'''
    return HttpResponse('<script>window.location="static/index.html"</script>')
   

