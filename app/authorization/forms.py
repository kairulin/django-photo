from django import forms
from . import models

class LoginForm(forms.Form):
    user_name = forms.CharField(label='帳號', max_length=10)
    password = forms.CharField(label='密碼', widget=forms.PasswordInput())