from django import forms
from django.contrib.auth.forms import AuthenticationForm
from driver.models import Driver
from django.contrib.auth.hashers import check_password


class nUserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Kullanıcı adı'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Parola'}))
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
class DriverLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Kullanıcı adı'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Parola'}))
    class Meta:
        model = Driver
        fields = ['username', 'password']
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data