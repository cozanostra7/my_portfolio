from django.forms import ModelForm
from django import forms
from . models import Messages

class contactForm(ModelForm):
    class Meta:
        model = Messages
        fields = ['name','email','message']

        widgets = {
            'name':forms.TextInput(attrs={
                'class':'input'
            }),
            'email':forms.EmailInput(attrs={
                'class':'input'
            }),
            'message':forms.Textarea(attrs={
                'class':'input'
            })
        }