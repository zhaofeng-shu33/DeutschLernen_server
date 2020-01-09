from django.http import HttpResponse,HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.html import escape

from .models import Word
from .xslt_render import xslt_render

class WordList(TemplateView):
    #model=Word
    template_name="word_list.html"
    def get_context_data(self, **kwargs):
        context_list =[]
        for i in Word.objects.all():
            context_list.append({'entry': i.entry, 'chinese': i.chinese})
        return {'object_list' : context_list}


def index(request):
    return HttpResponse('<script>window.location="static/index.html"</script>')
    #page redirection to index.html


def wordxml(request, wordform):
    '''return the word in xml form
    '''
    try:
        word = Word.objects.get(entry=wordform)
    except ObjectDoesNotExist as e:
        return HttpResponseNotFound("<h1>sorry {0} does not exist</h1>".format(escape(wordform)))
    return HttpResponse(word.xml, content_type="text/xml")

def wordhtml(request, wordform):
    '''return the word in html form
    '''
    try:
        word = Word.objects.get(entry=wordform)
    except ObjectDoesNotExist as e:
        return HttpResponseNotFound("<h1>sorry {0} does not exist</h1>".format(escape(wordform)))
    
    context = {}
    render_type = word.speech
    context['wordxml_render'] = xslt_render(word.xml, render_type)
    return render(request, 'search_word.html', context)

