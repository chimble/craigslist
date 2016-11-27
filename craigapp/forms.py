from django.contrib.auth.models import User
from django import forms
from craigapp.models import Craig, Ad


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class AdForm(forms.ModelForm):
    # def __init__(self, user):
    #     super(AdForm, self).__init__()
    class Meta:
        model = Ad
        fields = ['price', 'item']
