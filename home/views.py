from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.import
from home.forms import HomeForm
from home.models import Post, Friend
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForm()
        current_user = request.user
        posts = Post.objects.all().order_by('-created')
        users = User.objects.all()
        friends = current_user.friends.users.all()
        args = {'form':form, 'posts':posts , 'users':users , 'friends':friends }

        return render(request, self.template_name, args)

    def post(self , request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            text = form.cleaned_data['post']
            form = HomeForm()
            return redirect('home:home')

        args = {'form': form, 'text': text }
        return render(request, self.template_name,args)

@login_required()
def find_friendsview(request):
    template_name = 'home/find_friends.html'
    current_user = request.user
    users = User.objects.exclude(id=current_user.id)
    friends = current_user.friends.users.all()
    args = {'users': users, 'friends': friends}
    return render(request, template_name, args)

@login_required()
def add_friend(request, pk):
    current_user = request.user
    new_friend = User.objects.get(pk=pk)
    Friend.make_friend(current_user, new_friend)
    return redirect('home:find_friends')

@login_required()
def lose_friend(request, pk):
    current_user = request.user
    new_friend = User.objects.get(pk=pk)
    Friend.lose_friend(current_user, new_friend)
    return redirect('home:find_friends')
