from .forms import UserCreationFormWithEmail 
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms
# Create your views here.

class SignupView(CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SignupView,self).get_form()

        # Modificicacion en tiempo real 
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control',
        'placeholder':'Nombre de Usuario'})
        form.fields["email"].widget = forms.EmailInput(attrs={'class':'form-control',
        'placeholder':'Email Valido'}) 
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control',
        'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control',
        'placeholder':'Ingrese Contraseña'})
        
        return form