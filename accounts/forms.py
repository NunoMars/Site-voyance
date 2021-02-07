from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser
from django.utils.translation import ugettext_lazy as _


class CustomUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and password.
    """

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = CustomUser
        fields = ("email", _("first_name"), _("second_name"), _("phone_number"), _("send_email"), _("send_text_message"))
