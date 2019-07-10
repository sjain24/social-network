from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    location = forms.CharField(required=True)
    bio = forms.CharField(required=True)
    phone = forms.IntegerField(required=True)
    profile_pic = forms.FileField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'location'
                  , 'profile_pic', 'bio', 'phone', )

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class UpdateProfile(forms.ModelForm):
    location = forms.CharField(required=True)
    bio = forms.CharField(required=True)
    phone = forms.IntegerField(required=True)
    profile_pic = forms.FileField(required=False)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'location', 'phone', 'bio', 'profile_pic', )

