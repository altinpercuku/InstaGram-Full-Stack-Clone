from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login




# Login Request 

def login(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('homepage')
    
    else:
        form = CustomAuthenticationForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

# Register request

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('homepage')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)