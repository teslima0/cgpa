from datetime import date
from django import forms
from django.core import validators
from django.core.validators import RegexValidator
# creating a form 
import re

from django.forms.widgets import TextInput



class InputForm(forms.Form):
    pred=forms.CharField(label='Test Input', validators=[RegexValidator('^(\w+\d+|\d+\w+)+$', message="Password should be a combination of Alphabets and Numbers")]
    ,max_length=150, widget=forms.Textarea(attrs={'class':"form-control"}))

    def clean_pred(self):
         data= self.cleaned_data.get('pred')
         dig='[^0-9]'

         valid= re.match(data, dig)
         if not valid:
             raise forms.ValidationError('check your input')

         return data





class CgpCal(forms.Form):
    nums1 = forms.CharField(max_length=1, widget=TextInput(attrs={'pattern':'[A-Fa-f]'}))
    nums2= forms.CharField(max_length=1,  widget=TextInput(attrs={'pattern':'[0-9]+'}))
    nums3=forms.CharField(max_length=1,  widget=TextInput(attrs={'pattern':'[A-Fa-f]'}))
    nums4= forms.CharField(max_length=1,  widget=TextInput(attrs={'pattern':'[0-9]+'}))
    nums5= forms.CharField(max_length=1,  widget=TextInput(attrs={'pattern':'[A-Fa-f]'}))
    nums6=forms.CharField(max_length=1, widget=TextInput(attrs={'pattern':'[0-9]+'}))
    nums7 = forms.CharField(max_length=1, widget=TextInput(attrs={'pattern':'[A-Fa-f]'}))
    nums8= forms.CharField(max_length=1,  widget=TextInput(attrs={'pattern':'[0-9]+'}))
    nums9=forms.CharField(max_length=1,  widget=TextInput(attrs={'pattern':'[A-Fa-f]'}))
    nums10= forms.CharField(max_length=1,  widget=TextInput(attrs={'pattern':'[0-9]+'}))
    nums11= forms.CharField(max_length=1,  widget=TextInput(attrs={'pattern':'[A-Fa-f]'}))
    nums12 = forms.CharField(max_length=1, widget=TextInput(attrs={'pattern':'[0-9]+'}))
    nums13= forms.CharField(max_length=1,  widget=TextInput(attrs={'pattern':'[A-Fa-f]'}))
    nums14=forms.CharField(max_length=1,  widget=TextInput(attrs={'pattern':'[0-9]+'}))
    nums15= forms.CharField(max_length=1,  widget=TextInput(attrs={'pattern':'[A-Fa-f]'}))
    nums16= forms.CharField(max_length=1,  widget=TextInput(attrs={'pattern':'[0-9]+'}))
    nums17=forms.CharField(max_length=1, widget=TextInput(attrs={'pattern':'[A-Fa-f]'}))
    nums18 = forms.CharField(max_length=1, widget=TextInput(attrs={'pattern':'[0-9]+'}))
    nums19= forms.CharField(max_length=1,  widget=TextInput(attrs={'pattern':'[A-Fa-f]'}))
    nums20=forms.CharField(max_length=1,  widget=TextInput(attrs={'pattern':'[0-9]+'}))
    