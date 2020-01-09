from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import Word_edit.html_form_to_xml
from django.template import loader
import datetime
import code

def create_response(request):#WSGIRequest object,method has "get_full_path","get_host","get_port"
    """
    response for "Word_edit/create_new_word",GET to create new word, POST to update old word
    """
    #code.interact(local=locals())
    context={}
    rq=request.POST
    if rq:
        reqsheet = Word_edit.html_form_to_xml.parsegen(rq)
        Word_edit.html_form_to_xml.savedit(reqsheet)
        return HttpResponse('All right,click<a href="http://'+request.get_host()+request.get_full_path()+'">create another</a>')
        context['wordAddrchoice']=''
        context['isCreated']=''
    else:
        #Get Method here
        context['wordAddrchoice']='/Wort/'+str(Word_edit.html_form_to_xml.addWord('','','')+1)+'.xml'
        context['isCreated']='True'
    #You have submitted successfully.'<script>window.location="../../static/client_form/editing_interface.html"</script>'
    template = loader.get_template('Word_edit/editing_interface.html')
    return HttpResponse(template.render(context))
