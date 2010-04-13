# -*- coding: utf-8 -*-

# Create your forms here.

from django import forms

class UploadForm(forms.ModelForm):
    """
    Form para subir los ficheros.
    """
    name            = forms.CharField(label='Nombre', max_length=50)
    description     = forms.CharField(label='Descripción', widget=forms.Textarea, max_length=500)
    tags            = forms.CharField(label='Tags', max_length=50)
    data            = forms.FileField(label='Archivo', widget=forms.FileInput)
    replication     = forms.IntegerField(default=25, widget=forms.HiddenInput)    
    
    def __unicode__(self):
        return self.name

class ListForm(forms.ModelForm):
    """
    Form para listar los ficheros que tienen todos los tags especificados.
    """
    tags            = forms.CharField(label='Tags', max_length=50)
    
    def __unicode__(self):
        return self.tags

class SearchForm(forms.ModelForm):
    """
    Form para busqueda de texto libre.
    """
    text            = forms.CharField(label='Texto', max_length=250)
    
    def __unicode__(self):
        return self.text