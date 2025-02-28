from django.db import models

# Define a model with fields for name and email
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()