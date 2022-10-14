from django.forms import ModelForm, CharField

from apps.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
