'''
include part of speech, part of a unit(einheit)
'''
from django.db import models
from lxml import etree
SPEECH=(
        ('N','Substantiv'),
        ('V','Verben'),
        ('A','Adjektiv'),
        )
SPEECH_DIC = {i[0]:i[1] for i in SPEECH}
ANTEIL=(
    ('T', 'Text'),
    ('I', 'Intentionen'),
    ('L', 'Leseverstehen'),
    ('E','Einführung'),
    ('U','Übungen'),
    ('H','Hörverstehen'),
    ('O','Others'),
    )
class Word(models.Model):
    entry=models.CharField(max_length=30, primary_key = True)
    speech=models.CharField(max_length=1,choices=SPEECH,default='N')
    chinese=models.CharField(max_length=20)
    picture=models.CharField(max_length=30,null=True,blank=True)
    audio=models.CharField(max_length=30,null=True,blank=True)
    xml=models.TextField(null=True,blank=True)
    einheit=models.IntegerField(null=True,blank=True)
    anteil=models.CharField(max_length=1,choices=ANTEIL,default='T')
    def __str__(self):              # __unicode__ on Python 2
        return self.entry

def update_xml(obj):
    '''make xml string from other entries of object
    '''
    root = etree.Element('Entry')
    # pos attribute
    root.set('category', SPEECH_DIC[obj.speech])
    # entry
    entry = etree.SubElement(root, 'Stichwort')
    entry.text = obj.entry
    
    # chinese
    chinese_root = etree.SubElement(root, 'AllgemeineErläuterungen')
    eintrag = etree.SubElement(chinese_root, 'Eintrag')
    chinese_entry = etree.SubElement(eintrag, 'Chinesisch')
    chinese_entry.text = obj.chinese
    binary_xml_str = etree.tostring(root, pretty_print=True, xml_declaration = True, encoding="utf-8")
    return binary_xml_str.decode('utf-8')

