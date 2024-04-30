from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Utilisateur

class InscriptionForm(UserCreationForm):
    class Meta:
        model = Utilisateur
        fields = ['username', 'email', 'password1', 'password2']

class AchatForm(forms.Form):
    nombre_billets = forms.IntegerField(min_value=1, label="Nombre de billets")

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label="Nom d'utilisateur")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
