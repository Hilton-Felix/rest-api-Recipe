from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.conf import 


class UserCreationForm(UserCreationForm):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = "__all__"