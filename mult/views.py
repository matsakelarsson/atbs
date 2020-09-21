from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "mult/index.html")


def mats(request):
    return HttpResponse("Hello, Mats!")


def greet(request, name):
    return render(request, "mult/greet.html", {
        "name": name.capitalize()
    })