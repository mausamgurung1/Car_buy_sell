from django import forms
from.models import Location


class LocationForm(forms.ModelForm):
        class Meta:
                model = Location
                fields = {'address_1', 'address_2', 'city', 'state', 'zip_code'}
