from django.urls import path, re_path
from .views import signupaccount,logoutaccount,loginaccount

app_name = 'accounts'

urlpatterns = [
    path('sign-up',signupaccount,name='signup'),
    path('log-out',logoutaccount,name='logout'),
    path('login',loginaccount,name='login'),
]