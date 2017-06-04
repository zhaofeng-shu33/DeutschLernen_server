from django.shortcuts import render
from django.http import HttpResponse
#from jinja2 import Environment, PackageLoader
from django.template import loader
from Word_test import test_sampling
#import scoring
# Create your views here.
def test_config_response(request):
    #num_of_word_for_test=20
    #ability from sqlite3 user
    #word_list<-sqlite wordlist,all words verben Substantiv Adj
    #ability-difficulty>3,filter wordlist
    #['Abend','Apfel',..]
    #[-3,3]
    #Sampling returns ['Baum',..] len()=num_of_word_for_test;
    
    WordList=[]
    testtype=request.POST['test_type']
    t=test_sampling.generate_question(testtype)
    for i in range(len(t)):
        WordList.append({})
        WordList[i]['answer']=t[i][2]
        WordList[i]['question']=t[i][0]
        WordList[i]['choice']=t[i][1]
        WordList[i]['word']=t[i][3]
    #WordList.append({})
    #WordList[0]['wordform']='Abend'
    #WordList[0]['picture_location']='5.jpg'#or WordList[0]['chinese_translation']='aaa'
    #WordList[0]['choice']=['Abend','Alexanderplatz','Alkohol','Apotheke']
    #WordList.append({})
    #WordList[1]['wordform']='Baum'
    #WordList[1]['picture_location']='9.jpg'
    #WordList[1]['choice']=['Apfel','Abend','Baum','Anzeige']    
    context={}
    context['Word']=WordList
    #env = Environment(loader = PackageLoader('Word_test', 'jinja2'))
    #template = env.get_template('test_interface.html')
    #return HttpResponse(template.render(context))
    return render(request,'Word_test/test_interface.html',context)

def test_one_time(request):
    #return [Abend '1']['Baum' 0']
    #difficulty_vector=[difficulty of Abend,difficulty of Baum,
    #binary_vector=[1,0,..]
    #rq=request.POST
    #前端返回格式:正确的单词+是否答对
    #print(rq['word_1'])
    #print(rq['word_2'])
    #result=scipy.optimize.minimize_scalar(fun_to_maximize,bounds=(-3,3),method='bounded')
    #result.x is the ability,saved to user database
    #ability,ability uncertainly,
    return HttpResponse('Test ended');
