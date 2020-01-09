from django.contrib import admin
from django import forms

# Register your models here.
from DeutschLernen.models import Word, update_xml
class ContactForm(forms.ModelForm):
    class Meta:
        model=Word
        exclude=[]
@admin.register(Word)
class AuthorAdmin(admin.ModelAdmin):
    model=ContactForm
    fieldsets = (
    (None, {
        'fields': ('entry', 'chinese', 'speech')
    }),
    ('Advanced options', {
        'classes': ('collapse',),
        'fields': ('einheit','anteil','picture', 'xml'),
    }),
    )
    list_display=('entry','chinese')
    list_filter=('speech','einheit')
    def save_model(self, request, obj, form, change):
        if(obj.xml == ''):
            obj.xml = update_xml(obj)
        super().save_model(request, obj, form, change)
