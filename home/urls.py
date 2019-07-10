from . import views
from django.conf.urls import url
from django.urls import path
from home.views import HomeView
from django.contrib.auth.decorators import login_required
app_name = 'home'
# wrong username or password is their it will redirect to login1
urlpatterns = [
    path('', login_required(views.HomeView.as_view()), name='home'),
    path('find_friends/', views.find_friendsview, name='find_friends'),
    path('add_friend/<int:pk>/', views.add_friend, name='add_friend'),
    path('lose_friend/<int:pk>/', views.lose_friend, name='lose_friend'),
    # path('find_friends/<str:username>/', views.add_friendview, name='home'),
]