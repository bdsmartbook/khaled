from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'phone_number', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'input-create'})
        self.fields['phone_number'].widget.attrs.update({'class': 'input-create'})
        self.fields['email'].widget.attrs.update({'class': 'input-create'})
        self.fields['phone_number'].label = 'Phone'

