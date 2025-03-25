from django.db import models
import django

class ActivityModel(models.Model):
       action = models.CharField(max_length=1024)
       datetime = models.DateTimeField(default=django.utils.timezone.now)
       #time = models.TimeField(default=django.utils.timezone.now)