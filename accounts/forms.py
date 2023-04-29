from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.core.exceptions import ValidationError

# Sign Up Form
class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=100, required=True, help_text='Enter username, Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.')
    first_name = forms.CharField(max_length=30, required=True, help_text='Enter First Name')
    last_name = forms.CharField(max_length=30, required=True, help_text='Enter Last Name')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = (
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2', 
        )
    # def __init__(self, *args, **kwargs):
    #     super(SignUpForm, self).__init__(*args, **kwargs)

    #     for fieldname in ['first_name', 'last_name']:
    #         self.fields[fieldname].help_text = None