from jinja2 import Environment, PackageLoader
from Word_test import test_sampling
env = Environment(loader = PackageLoader('Word_test', 'templates'))
template = env.get_template('test_interface.html')
WordList=[]
t=test_sampling.generate_question('chinese')
for i in range(len(t)):
    WordList.append({})
    WordList[i]['answer']=t[i][2]
    WordList[i]['question']=t[i][0]
    WordList[i]['choice']=t[i][1]
    WordList[i]['word']=t[i][3]
context={}
context['Word']=WordList
print(template.render(context))
