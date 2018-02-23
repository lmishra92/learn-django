from django import forms
from .models import RestaurantLocation

class RestaurantLocationForm(forms.ModelForm):
    class Meta:
        model = RestaurantLocation
        fields = ['name', 'location', 'category']

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == 'Hello':
            raise forms.ValidationError("Not a valid name")
        return name

class RestaurantCreateForm(forms.Form):
    name     = forms.CharField()
    location = forms.CharField(required=True)
    category = forms.CharField(required=True)

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == 'Hello':
            raise forms.ValidationError("Not a valid name")
        return name

shopping_type = (
    ('pickup', 'Pickup'),
    ('delivery', 'Home Delivery')
)
class ShoppingForm(forms.Form):
    postcode = forms.CharField(label="Enter your postcode", max_length=6)
    shopping_type = forms.ChoiceField(required=True,
                                      widget=forms.RadioSelect,
                                      choices=shopping_type)
