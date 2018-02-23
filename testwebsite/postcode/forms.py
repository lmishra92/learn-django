from django import forms
from utils.zipcodetrigger import ZipCodeTrigger

class PostCodeForm(forms.Form):
    postcode = forms.CharField(label='Enter your postcode', max_length=10)

