from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login, authenticate



# Create your views here.


def login(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('homepage')
    
    else:
        form = CustomAuthenticationForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)