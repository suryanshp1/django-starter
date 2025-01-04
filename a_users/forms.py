from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
            'avatar': forms.FileInput(),
            'displayname': forms.TextInput(attrs={'placeholder': 'Add display name'}),
            'info': forms.Textarea(attrs={'placeholder': 'Add information', "rows": 3}),
        }


class EmailForm(ModelForm):
    class Meta:
        model = User
        fields = ['email']