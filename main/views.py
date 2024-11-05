from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required


# @login_required(login_url='login_page')
def home(request):
    return render(request, 'main/home.html')

