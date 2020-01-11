from django.shortcuts import render
from django.http import HttpResponse
from .html_form_to_xml import parsegen, savedit, addWord
from django.template import loader

def create_response(request):
    """
    response for "Word_edit/create_new_word",GET to create new word, POST to update old word
    """
    context={}
    rq = request.POST
    if rq:
        reqsheet = parsegen(rq)
        savedit(reqsheet)
        return HttpResponse('All right,click<a href="http://'+request.get_host()+request.get_full_path()+'">create another</a>')
    else:
        # GET Method here
        context['wordAddrchoice'] = '/Wort/' + str(addWord('', '', '') + 1) + '.xml'
        context['isCreated'] = 'True'
    template = loader.get_template('Word_edit/editing_interface.html')
    return HttpResponse(template.render(context))
