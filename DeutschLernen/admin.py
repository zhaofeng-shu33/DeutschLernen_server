from django.contrib import admin
from django import forms

# Register your models here.
from DeutschLernen.models import Word
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

