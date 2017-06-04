import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DeutschLernen.settings")
import django
django.setup()
from django.template import loader
template = loader.get_template('child.html')
entry_1={}
entry_1['title']='title_1';
entry_1['body']='body_1';
entry_2={}
entry_2['title']='title_2';
entry_2['body']='body_2';

context={}
context['blog_entries']=[entry_1,entry_2]
print(template.render(context))
