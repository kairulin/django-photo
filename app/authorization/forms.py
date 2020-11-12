from django import forms
from . import models

class LoginForm(forms.Form):
    username = forms.CharField(label='您的姓名', max_length=10)
    password = forms.CharField(label='密碼', widget=forms.PasswordInput())