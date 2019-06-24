# coding: utf-8

from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

# Create your forms here.

from formset_app.models import *
from django.apps import apps



class MetaForm(forms.ModelForm):
    class Meta:
        model = apps.get_model('scan_api', 'JobEntry')
        # model = Entry
        fields = '__all__'
        # widgets = {'job_time': forms.HiddenInput()}
