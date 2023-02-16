# -*- encoding: utf-8 -*-

from django import forms

class AddressForm(forms.Form):
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Address",
                "class": "form-control"
            }
        ))