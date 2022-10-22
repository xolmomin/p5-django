from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField, EmailField, Form

from apps.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class LoginForm(Form):
    username = CharField(max_length=255)
    password = CharField(max_length=255)

    def clean_username(self):
        username = self.cleaned_data['username']
        if not User.objects.filter(username=username):
            # self.add_error('username', 'The username is not found !')
            raise ValidationError('The username is not found !')
        return username


class CustomUserCreationForm(UserCreationForm):
    email = EmailField(max_length=255, label='Email')

    class Meta:
        model = User
        fields = ('username', 'email')
