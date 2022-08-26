from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return HttpResponse("Welcome to About-Us page!")