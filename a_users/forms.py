from django.forms import ModelForm
from django import forms
from .models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
            'avatar': forms.ImageField(widget=forms.FileInput()),
            'displayname': forms.TextInput(attrs={'placeholder': 'Add display name'}),
            'info': forms.Textarea(attrs={'placeholder': 'Add information', "rows": 3}),
        }