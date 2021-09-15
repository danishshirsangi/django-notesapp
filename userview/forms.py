from django.db import models
from django.forms import widgets
from django.http import request
from .models import semOne
from django import forms

class semoneControl(forms.ModelForm):
    class Meta:
        model = semOne
        fields = ['select_sub','module_name','pdf_module']

        labels = {'select_sub':'','module_name':'','pdf_module':''}
        
        widgets = {
            'select_sub':forms.Select(attrs={'class':'form-select w-50 mx-auto my-2'}),
            'module_name':forms.TextInput(attrs={'class':'form-control w-50 mx-auto my-2','placeholder':'Module Name'}),
            'pdf_module':forms.FileInput(attrs={'class':'form-control w-50 mx-auto my-2'})
            }