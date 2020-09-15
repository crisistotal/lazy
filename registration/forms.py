from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Debe ser un mail de verdad")

    class Meta:
        model = User
        fields = ("username","email","password1","password2")

    def clean_email(self):
        'metodo para validar el mail'
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El Email ya esta registrado, prueba con otro")
        return email

    def clean_username(self):
        """
        Metodo para validiar Usuario
        """    
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("El Usuario ya existe, intenta con otro")

        return username



