from django import forms
from captcha.fields import CaptchaField

from marketplace.models import ContactUsModel

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = ContactUsModel
        fields = ['email', 'subject', 'message']