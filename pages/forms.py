from django import forms
from .models import Ticket


class ContactForm(forms.ModelForm):
    text = forms.TextInput()

    class Meta:
        model = Ticket
        fields = ('first_name', 'last_name', 'email', 'text',)
