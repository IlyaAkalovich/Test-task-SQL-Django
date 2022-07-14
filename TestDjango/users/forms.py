from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Shortener

User = get_user_model()

class ShortenerForm(forms.ModelForm):
    long_url = forms.URLField(widget=forms.URLInput(
        attrs={"class": "form-control form-control-lg", "placeholder": "Your URL to shorten"}))

    class Meta:
        model = Shortener

        fields = ('long_url')



class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User


