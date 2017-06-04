import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DeutschLernen.settings")
import django
from lxml import etree
##f=open('E:/DeutschLernen/Deutsch-Lernen/Deutsch-Lernen/Wordlist_11.xml','rb')


django.setup()
from DeutschLernen.models import Word
i=1
while(i<465):
    f=open('E:/DeutschLernen/Deutsch-Lernen/Deutsch-Lernen/Wort/%d.xml'%i,'rb')
    st=f.read()
    root=etree.fromstring(st)
    u=Word.objects.get(xml_file_name='N'+str(i)+'.xml')
    print(root[1].text)
    u.einheit=int(root[1].text)
    u.save()
    i=i+1

##while(i<465):
##    f=open('E:/DeutschLernen/Deutsch-Lernen/Deutsch-Lernen/Wort/%d.xml'%i,'rb')
##    root=etree.fromstring(f.read())
##    if(root[0].attrib.has_key('Bild')):
##        root[0].attrib.pop('Bild')
##    if(root[0].attrib.has_key('Audio')):
##        root[0].attrib.pop('Audio')
##    root.remove(root.find('Einheit'))
##    root.remove(root.find('Anteil'))
##    st=etree.tostring(root,encoding='utf-8',pretty_print=True).decode('utf-8')
##    u=Word.objects.filter(xml_file_name='N%d.xml'%i)[0]
##    #u.entry=root[i].text
##    #u.chinese=root[i].get('chinese')
##    u.xml=st
##    u.save()
##    i=i+1

