from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import  Word_edit.html_form_to_xml
from .forms import NameForm,ArticleForm
from DeutschLernen.models import Word
from django.forms import formset_factory
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

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            #send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/static/css/style.css')
    # if a GET (or any other method) we'll create a blank form
    else:
        a=request.GET.get('word')
        b=None;
        if(a):
            b=Word.objects.get(entry=a)
        if(b):
            form=NameForm(instance=b)
        else:
            form = NameForm()
            #ArticleFormSet=formset_factory(ArticleForm)

    return render(request, 'Word_edit/name.html', {'form': form})
    #return render(request,'Word_edit/manage_articles.html',{'formset':formset})
def manage_articles(request):
    ArticleFormSet=formset_factory(ArticleForm,extra=2,can_order=True,can_delete=True)
    if request.method == 'POST':
        formset=ArticleFormSet(request.POST)
        if formset.is_valid():
            return HttpResponse("valid")
    else:
        formset=ArticleFormSet(initial=[{
            'title':'test',
            'pub_date':datetime.date.today(),}])
    return render(request,'Word_edit/manage_articles.html',{'formset':formset})
            
    
