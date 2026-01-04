from django.shortcuts import render


def homepage(request):
    return render(request, "homepage.html")


def blog(request):
    return render(request, "blog.html")
