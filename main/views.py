from django.shortcuts import render, HttpResponse


def home(request):
    return HttpResponse("<h1>ongoing build</h1>")

