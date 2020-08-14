from django import forms

from django_registration.forms import RegistrationForm

from profiles.models import User

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext, gettext_lazy as _

class CustomUserForm(RegistrationForm):

    class Meta(RegistrationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args,**kwargs)
        self.fields['first_name'].error_messages = {'required': 'This field is required'}
        self.fields['last_name'].error_messages = {'required': 'This field is required'}



