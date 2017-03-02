from django.shortcuts import render
from django.http import HttpResponse
import json
import nltk
from DeutschLernen import settings
corpus_root_dir=settings.STATICFILES_DIRS[0]+'Text/'
my_reader=nltk.corpus.reader.PlaintextCorpusReader(root=corpus_root_dir,fileids=r'Text[0-9]+-[12AB].txt',encoding='utf-8')
my_words=my_reader.words()
example_index=nltk.text.ConcordanceIndex(my_words)
# Create your views here.
def example_response(request):
    rq=request.GET
    queried_word=rq['queried_word']
    Ls=example_index.offsets(queried_word)
    Ls.extend(example_index.offsets(queried_word[0].upper()+queried_word[1:len(queried_word)]))
    response_data = {}
    if(len(Ls)>0):
        example_list=[]
        for i in range(1,len(Ls)+1):
            st_pre=' '.join(my_words[(Ls[i-1]-20):Ls[i-1]])
            st_after=' '.join(my_words[(Ls[i-1]+1):(Ls[i-1]+20)])
            st_current='<span style="color:red">'+my_words[Ls[i-1]]+'</span>'
            example_list.append(st_pre+' '+st_current+' '+st_after)
        response_data['example_list'] =example_list  
    return HttpResponse(json.dumps(response_data),content_type="application/json")
