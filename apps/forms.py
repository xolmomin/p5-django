from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, CharField, EmailField

from apps.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
    email = EmailField(max_length=255, label='Email')

    class Meta:
        model = User
        fields = ('username', 'email')
