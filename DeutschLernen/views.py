from django.http import HttpResponse,HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views.generic import TemplateView
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
    '''handles all root xml files request
    '''
    try:
        word = Word.objects.get(entry=wordform)
    except ObjectDoesNotExist as e:
        return HttpResponseNotFound("<h1>sorry " + wordform + " does not exist</h1>")
    return HttpResponse(word.xml, content_type="text/xml")
def wordhtml(request, wordform):
    '''handles all root html pages request
    '''
    if(root_page_name=='search_word.html'):
        wordlist=[]
        for i in Word.objects.all():
            wordlist.append({'wordform':i.entry,'address':i.xml_file_name})
        context={}
        for i in Website_Text.objects.all():
            context[i.key]=i.chinese
        context['wordlist']=wordlist
        query=request.GET
        wordAddress=query.get('wordAddress')
        a=None;
        if(wordAddress):
            a=Word.objects.filter(xml_file_name=wordAddress)
        elif(query.get('wordform')):
            a=Word.objects.filter(entry=query.get('wordform'))
        if(a):
            render_type='V'
            if(query.get('edit')):
                render_type='E'
            context['wordxml_render']=xslt_render(a[0].xml,'N'+render_type)
        return render(request,root_page_name,context)
    return HttpResponse("Your request root page name is "+root_page_name)
