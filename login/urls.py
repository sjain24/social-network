from . import views
from django.urls import path
from django.conf.urls import url,include
#from django.conf.urls import url
#from django.contrib.auth import views as auth_views

app_name = 'login'
# wrong username or password is their it will redirect to login1
urlpatterns = [
    path('', views.login.as_view(), name='login'),
    path('&&/signup/', views.UserFormView.as_view(), name='register'),
    path('&&/logout/', views.user_logout, name = 'logout'),
    path('<str:username>/', views.home, name='home'),
    path('<str:username>/edit/', views.edit_profile, name='edit_profile'),
    

]

#url(r'(?P<username>)/$', views.home, name='home')
#path('<str : username>/', views.home, name='home')