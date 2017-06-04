from django.forms import ModelForm
from django import forms
from DeutschLernen.models import Word
from django.utils.translation import ugettext_lazy as _
BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
FAVORITE_COLORS_CHOICES = (
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
)
class NameForm(ModelForm):
    class Meta:
        model=Word
        fields=['xml_file_name','entry','chinese','speech','picture','audio','xml']
        help_texts={
            'xml':_('xml code representation'),
            }

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    pub_date=forms.DateField()
