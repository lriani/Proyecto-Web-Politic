from django import forms
from .models import UserBase
from django.contrib.auth.forms import (AuthenticationForm)


class UserLoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'login-username'}))
    password = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'login-pwd',
        }
    ))

class RegistrationForm(forms.ModelForm):

    user_name = forms.CharField(label='Nombre de usuario', min_length=4, max_length=50, help_text='Requerido')
    email = forms.EmailField(label='email', max_length=100, help_text='Requerido', error_messages={'Requerido': 'Lo lamento, necesitas colocar un email'})
    password= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repite contraseña', widget=forms.PasswordInput)

    class Meta:
        model = UserBase
        fields = ('user_name', 'email')

    def clean_username(self):
        user_name = self.cleaned_data['user_name'].lower()
        r = UserBase.objects.filter(user_name=user_name)
        if r.count():
            raise forms.ValidationError("El usuario ya existe")
            return user_name
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Contraseña incorrecta')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if UserBase.objects.filter(email=email).exists():
            raise forms.ValidationError('Por favor coloque otro mail, éste ya fue usado')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Usuario'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Contraseña'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Repite contraseña'})
                   