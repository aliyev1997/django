from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import *
from django import forms

class AddPostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'

class AddCommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields='__all__'



class Reqistration(UserCreationForm):
    class Meta:
        model=Account
        fields=('email','username',)


class LoginUserForm(AuthenticationForm):

    password=forms.CharField()