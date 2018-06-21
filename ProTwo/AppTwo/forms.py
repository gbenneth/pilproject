#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May  1 17:06:34 2018

@author: genebenneth
"""

from django import forms
from AppTwo.models import customer

class NewUserForm(forms.ModelForm):
    class Meta():
        model = customer
        fields = '__all__'
        
class UploadFileForm(forms.Form):
    file = forms.ImageField()