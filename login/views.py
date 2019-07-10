from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.views.generic import View
from django.contrib.auth.models import User
from login.forms import UserRegisterForm, UpdateProfile
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from home.models import Friend
# from django.contrib.auth.forms import UserChangeForm
# from django.contrib.auth.decorators import login_required
# from .models import UserProfile
# from .models import User
# from django.contrib.auth.models import User
from django.http import HttpResponse
# from .forms import UserRegisterForm
# from django.views import generic
# # from django.conf import settings
#
#
# def profile(request, username):
#     user = get_object_or_404(User, username=username)
#     return redirect(reverse('login:home', kwargs={'username': username}), {'user': user})


def home(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'profile/index2.html', {'user': user})


class login(View):
    template_name = 'login/index.html'

    def get(self, request):
        return render(request, self.template_name, {})

    def post(self, request):
        username1 = request.POST['username1']
        password1 = request.POST['password1']
        user = authenticate(username=username1, password=password1)
        if user is not None:
            auth_login(request, user)
            return redirect(reverse('home:home'))
        else:
            return render(request, self.template_name, {})


class UserFormView(View):
    form_class = UserRegisterForm
    template_name = 'login/signup.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'user' : form})

    def post(self, request):
        form = self.form_class(request.POST , request.FILES)

        if form.is_valid():
            user = form.save()
            user.profile.location = self.request.POST["location"]
            user.profile.bio = self.request.POST["bio"]
            user.profile.phone = self.request.POST["phone"]
            user.profile.profile_pic = self.request.FILES["profile_pic"]
            # user.make_friend(user)
            user.profile.save()
            Friend.make_friend(user)
            auth_login(request, user)
            return redirect(reverse('login:home', kwargs={"username": user.username}), {'user': user})
        else:
            return render(request, self.template_name, {'user': form})


@login_required
def edit_profile(request, username):
    user = get_object_or_404(User, username=username)
    if request.user == user:
        if request.method == "POST" :
            form = UpdateProfile(request.POST , request.FILES)
            if form.is_valid():
                user.first_name = request.POST["first_name"]
                user.last_name = request.POST["last_name"]
                user.email = request.POST["email"]
                user.profile.location = request.POST["location"]
                user.profile.bio = request.POST["bio"]
                user.profile.phone = request.POST["phone"]
                if request.FILES:
                    user.profile.profile_pic = request.FILES["profile_pic"]
                user.save()
                user.profile.save()
                return redirect(reverse('login:home', kwargs={"username": user.username}), {'user': user})
            else:
                return render(request, 'profile/edit_profile.html', {'user': user})

        else:
            return render(request, 'profile/edit_profile.html', {'user': user})
    else:
        return redirect(reverse('login:home', kwargs={"username": user.username}), {'user': user})

def user_logout(request):
    request.user
    logout(request)
    return redirect(reverse('login:login'))

















