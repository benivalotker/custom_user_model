from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, get_user_model, login, logout

def login_(request):
    form = UserLoginForm(request.POST or None)

    if request.user.is_authenticated:
        return redirect('football_index')
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('football_index')    
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form})

    return render(request, 'login.html', context={'form': form, 'title': 'Login Page'})


def register_(request):
    form = UserRegisterForm(request.POST or None)
    
    if request.user.is_authenticated:
        return redirect('football_index')
    if form.is_valid():
        
        user = form.save(commit=False)              
        
        password = form.cleaned_data.get('password')
        
        user.set_password(password)
        
    
        user.save()
        new_user = authenticate(username=user.username, password=password)
        
        if new_user is not None:
            # save user object in session
            login(request, new_user)   
            return redirect('football_index')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', context={'form': form, 'title': 'Register Page'})


def logout_(request):
    logout(request)
    return redirect('users_login')