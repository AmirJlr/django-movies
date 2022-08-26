from django.shortcuts import render
from django.http import HttpResponse
from .models import News
# Create your views here.

def news(request):
    newss=News.objects.all()
    context={
        'newss':newss,
    }
    return render(request, 'news/news.html',context)