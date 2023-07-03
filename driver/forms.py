from django import forms
from .models import Driver

class DriverUpdateForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['ad', 'soyad', 'aciklama', 'adres', 'email', 'telefon', 'profil_fotografi', 'arac_marka_model', 'calistigi_sehirler', 'gunluk_tur_fiyati', 'availability_start', 'availability_end']
        widgets = {
            'ad': forms.TextInput(attrs={'class': 'form-control'}),
            'soyad': forms.TextInput(attrs={'class': 'form-control'}),
            'aciklama': forms.Textarea(attrs={'class': 'form-control'}),
            'adres': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefon': forms.TextInput(attrs={'class': 'form-control'}),
            'profil_fotografi': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'arac_marka_model': forms.TextInput(attrs={'class': 'form-control'}),
            'calistigi_sehirler': forms.TextInput(attrs={'class': 'form-control'}),
            'gunluk_tur_fiyati': forms.NumberInput(attrs={'class': 'form-control'}),
            'availability_start': forms.DateInput(attrs={'class': "form-control date", 'data-provide': "datepicker", 'data-date-language': 'tr', 'data-date-format': 'dd/mm/yyyy'}),
            'availability_end': forms.DateInput(attrs={'class': "form-control date", 'data-provide': "datepicker", 'data-date-language': 'tr', 'data-date-format': 'dd/mm/yyyy'}),
       }
    
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
    
    def save(self, commit=True):
        if self.is_valid():
            driver = super().save(commit=False)
            if commit:
                driver.save()
            return driver
        return None
