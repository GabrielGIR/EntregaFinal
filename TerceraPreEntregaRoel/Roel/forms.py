from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from django.forms.forms import Form  
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from .models import *

class formSetCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'email']


class formSetDistri(forms.Form): #distribuidora

    nombre = forms.CharField(max_length=30)

    apellido = forms.CharField(max_length=30)

    email = forms.EmailField()

    profesion = forms.CharField(max_length=30)

class formSetLocal(forms.Form): #distribuidora

    nombre = forms.CharField(max_length=30)

    calle = forms.CharField(max_length=30)

    país = forms.CharField(max_length=30)

class formSetOrden(ModelForm):
    class Meta:
        model = Ordenar
        fields = ['producto', 'estado', 'cliente'] 

    def __init__(self, *args, **kwargs):
        super(formSetOrden, self).__init__(*args, **kwargs)
        self.fields['cliente'].widget = forms.widgets.Select(attrs={'class': 'form-control'})



class CustomUserCreationForm(UserCreationForm):  
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']

class UserEditForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Email"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Primer nombre"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Apellido"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password"}))

    class Meta:
        model= User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
        help_texts = {k:"" for k in fields}

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label="" ,widget=forms.PasswordInput(attrs={"placeholder":"Old Password"}))
    new_password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={"placeholder":"New Password"}))
    new_password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={"placeholder":"Confirmation New Password"}))

    class Meta:
        model= User
        fields = ['old_password', 'new_password1', 'new_password2']
        help_texts = {k:"" for k in fields}


class AvatarForm(forms.Form):
    avatar = forms.ImageField()


class PostForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2}), required=True)
    class Meta:
        model = Post
        fields = ['content']