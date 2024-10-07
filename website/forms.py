from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']        

class CustomUserChangeForm(forms.ModelForm):
    
    password = forms.CharField(
        widget=forms.PasswordInput,
        required=False,  
        label='New Password'
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        required=False,
        label='Confirm Password'
    )

    class Meta:
        model = User
        fields = ['username', 'email']

    def save(self, commit=True):
        user = super(CustomUserChangeForm, self).save(commit=False)

        if self.cleaned_data['password']:
            user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()
        return user