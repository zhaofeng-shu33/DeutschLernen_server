from django.shortcuts import render
from django.http import HttpResponse
import  Word_edit.html_form_to_xml

def create_response(request):
    rq=request.POST
    reqsheet=Word_edit.html_form_to_xml.parsegen(rq)
    Word_edit.html_form_to_xml.savedit(reqsheet)
    #You have submitted successfully.
    return HttpResponse('<script>window.location="../../static/client_form/editing_interface.html"</script>')
# Create your views here.
def query_response(request):
    rq=request.GET
    query_str=rq.get('query')
    myresponse=HttpResponse('Your query is '+query_str)
    myresponse.__setitem__('X-XSS-Protection',0)
    return myresponse
