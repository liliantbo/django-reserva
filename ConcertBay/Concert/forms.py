from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for key in self.fields.keys():
            self.fields[key].widget.attrs['class'] = 'general'

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegistroForm, self).__init__(*args, **kwargs)
        for key in self.fields.keys():
            self.fields[key].widget.attrs['class'] = 'general'

    def save(self, commit=True):
        user = super(RegistroForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.save()
        return user
