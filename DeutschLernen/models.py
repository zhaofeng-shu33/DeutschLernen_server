from django.db import models
SPEECH=(
        ('N','Substantiv'),
        ('V','Verben'),
        ('A','Adjektiv'),
        )
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
    xml_file_name=models.CharField(max_length=10,primary_key=True)
    entry=models.CharField(max_length=30)
    speech=models.CharField(max_length=1,choices=SPEECH,default='N')
    chinese=models.CharField(max_length=20)
    picture=models.CharField(max_length=30,null=True,blank=True)
    audio=models.CharField(max_length=30,null=True,blank=True)
    xml=models.TextField(null=True,blank=True)
    einheit=models.IntegerField(null=True,blank=True)
    anteil=models.CharField(max_length=1,choices=ANTEIL,default='T')
    def __str__(self):              # __unicode__ on Python 2
        return self.entry

class Website_Text(models.Model):
    key=models.CharField(max_length=20,primary_key=True)
    chinese=models.CharField(max_length=200)
