from django.urls import path
from . import views

urlpatterns = [
    path("past_projects", views.past_projects, name="past_projects"),
]
