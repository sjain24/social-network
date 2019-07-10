from django import forms
from django.forms import ModelForm
from home.models import Post


class HomeForm(forms.ModelForm):
    post = forms.CharField(required=True)

    class Meta:
        model = Post
        fields = {'post',}