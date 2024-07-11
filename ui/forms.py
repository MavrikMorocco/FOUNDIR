# ui/forms.py
from django import forms

class SearchForm(forms.Form):
    name = forms.CharField(max_length=100, required=False, help_text='Enter a name to search.')
    image = forms.ImageField(required=False, help_text='Upload an image to search.')

