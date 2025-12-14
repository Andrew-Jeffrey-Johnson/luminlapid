from django.shortcuts import render


def past_projects(request):
    return render(request, "past_projects.html")
