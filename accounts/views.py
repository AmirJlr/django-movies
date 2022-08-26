from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.db import IntegrityError

from .forms import UserCreateForm

from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm


from django.contrib.auth.decorators import login_required

# Create your views here.


def signupaccount(request):
    if request.method == 'GET':
        return render(request, 'accounts/signup.html', {'form': UserCreateForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('movie:home')
            except IntegrityError:
                return render(request, 'accounts/signup.html', {'form': UserCreateForm,
                                                                'error': 'Username is already exists.try another one.'})

        else:
            return render(request, 'accounts/signup.html', {'form': UserCreateForm,
                                                            'error': 'passwords do not match'})

def loginaccount(request):
    if request.user.is_authenticated:
        return redirect('movie:home')
        
    if request.method == 'GET':
        return render(request, 'accounts/login.html',{'form':AuthenticationForm})
    
    else:
        user = authenticate(request,username=request.POST['username'],
        password = request.POST['password'])

        if user is None:
            return render(request, 'accounts/login.html',{'form':AuthenticationForm(),
            'error':'username and password do not match'})
        else :
            login(request, user)
            return redirect('movie:home')


@login_required
def logoutaccount(request):
    logout(request)
    return redirect('movie:home')
