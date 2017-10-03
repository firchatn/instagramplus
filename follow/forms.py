from django import forms

class accesForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'username'}),label='')
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': 'password'}),label='')