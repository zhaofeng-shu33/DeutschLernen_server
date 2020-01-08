from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import render
from .models import Word,Website_Text
from .xslt_render import xslt_render
from django.views.generic import TemplateView

class WordList(TemplateView):
    #model=Word
    template_name="word_list.html"
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        a=None
        if(self.request.GET):
            a=self.request.GET.get('wordAddress')
            print(a)
        context ={}
        # Add in a QuerySet of all the books
        for i in Website_Text.objects.all():
            context[i.key]=i.chinese
        return context

def index(request):
    return HttpResponse('<script>window.location="static/index.html"</script>')
    #page redirection to index.html

def wordxml(request,xml_file):
    a=Word.objects.filter(xml_file_name=xml_file)
    if(a):
        return HttpResponse(a[0].xml,content_type="text/xml")
    else:
        return HttpResponseNotFound("<h1>sorry "+xml_file+" does not exist</h1>")

def root_page_request(request,root_page_name):
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
        a = None
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
