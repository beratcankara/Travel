import re
from django import forms
from nUser.models import nUser
from requests import session
from driver.models import Driver, Image
from multiupload.fields import MultiFileField
from django.contrib.auth.hashers import make_password
class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
    
    def save(self, commit=True):
        if self.is_valid():
            driver = super().save(commit=False)
            driver.password = make_password(self.cleaned_data["password"])
            if commit:
                driver.save()
            return driver
        return None
class imageForm(forms.Form):
    images = MultiFileField(min_num=1, max_num=10)
    class Meta:
        model = Image
        fields = '__all__'
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
    
    

class RegistrationForm(forms.Form):
    tc_kimlik = forms.CharField(max_length=11)
    adres = forms.CharField(widget=forms.Textarea)
    telefon = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    username = forms.CharField(label="Lütfen kullanıcı adınızı giriniz.", max_length=50)
    password1 = forms.CharField(widget=forms.PasswordInput, max_length=20, label="Lütfen şifre giriniz.")
    password2 = forms.CharField(widget=forms.PasswordInput, max_length=20, label="Lütfen şifrenizi doğrulayın.")

    def clean_username(self):
        username = self.cleaned_data.get('username', '')
        if ' ' in username:
            raise forms.ValidationError('Kullanıcı adı boşluk içeremez.')
        if not re.match(r'^\w+$', username):
            raise forms.ValidationError('Kullanıcı adı yasaklı karakterler içeremez.')
        if nUser.objects.filter(username=username).exists():
            raise forms.ValidationError('Bu kullanıcı adı zaten kullanımda.')
        return username

    def clean_tc_kimlik(self):
        tc_kimlik = self.cleaned_data.get('tc_kimlik', '')
        if len(tc_kimlik) != 11:
            raise forms.ValidationError('TC Kimlik 11 karakter olmalıdır.')
        return tc_kimlik

    def clean_adres(self):
        adres = self.cleaned_data.get('adres', '')
        if len(adres.split()) < 5:
            raise forms.ValidationError('Adres en az 5 kelime içermelidir.')
        return adres

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1', '')
        password2 = self.cleaned_data.get('password2', '')
  
        if password1 != password2:
            raise forms.ValidationError('Şifreler eşleşmiyor.')
        return password2

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
    
    def save(self):
        if self.is_valid():
            user = nUser(
                username=self.cleaned_data['username'],
                tc_kimlik=self.cleaned_data['tc_kimlik'],
                adres=self.cleaned_data['adres'],
                telefon=self.cleaned_data['telefon'],
                email=self.cleaned_data['email'],
                first_name=self.cleaned_data['first_name'],
                last_name=self.cleaned_data['last_name'],
            )
            user.set_password(self.cleaned_data['password2'],)
            user.save()
            return user
        return None
