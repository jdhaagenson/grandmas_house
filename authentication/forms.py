from django import forms
from django.forms import ModelForm
from beneficiary.models import Beneficiary, Executor


class AddBeneficiaryForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    profile_pic = forms.ImageField(widget=forms.ClearableFileInput)
    class Meta:
        model = Beneficiary
        fields = ['username', 'email', 'display_name', 'profile_pic', 'password']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=80)
    password = forms.CharField(widget=forms.PasswordInput)


class AddExecutorForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    profile_pic = forms.ImageField(widget=forms.ClearableFileInput)
    class Meta:
        model = Executor
        fields = ['username', 'email', 'display_name', "profile_pic", "password"]