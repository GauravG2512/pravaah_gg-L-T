from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from apps.users.models import User

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=150, 
        required=True, 
        widget=forms.TextInput(attrs={
            'class': 'glass-input w-100',
            'placeholder': 'First Name'
        })
    )
    middle_name = forms.CharField(
        max_length=150, 
        required=False, 
        widget=forms.TextInput(attrs={
            'class': 'glass-input w-100',
            'placeholder': 'Middle Name'
        })
    )
    last_name = forms.CharField(
        max_length=150, 
        required=True, 
        widget=forms.TextInput(attrs={
            'class': 'glass-input w-100',
            'placeholder': 'Last Name'
        })
    )
    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(attrs={
            'class': 'glass-input w-100',
            'placeholder': 'Email Address'
        })
    )
    contact = forms.CharField(
        max_length=15, 
        required=True, 
        widget=forms.TextInput(attrs={
            'class': 'glass-input w-100',
            'placeholder': 'Contact Number'
        })
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'middle_name', 'last_name', 'email', 'contact')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email address already exists.")
        return email

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={
            'class': 'glass-input w-100',
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'glass-input w-100',
            'placeholder': 'Password'
        })
    )
