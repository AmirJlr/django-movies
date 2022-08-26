from django.urls import path, re_path
from .views import news

app_name = 'news'

urlpatterns = [
    path('',news , name='news')
]