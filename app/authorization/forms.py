from django import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    user_name = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'autocomplete': 'new-account'})
    )
    password = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'})
    )


class RegisterForm(UserCreationForm):
    user_name = forms.CharField(
        label="帳號",
        max_length=150,
        widget=forms.TextInput(attrs={'autocomplete': 'new-account'})
    )

    error_messages = {
        'password_mismatch': ('密碼不一致'),
    }
    password1 = forms.CharField(
        label=("密碼"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),

    )
    password2 = forms.CharField(
        label=("確認密碼"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )

    class Meta:
        model = User
        fields = ('user_name', 'password1', 'password2')
