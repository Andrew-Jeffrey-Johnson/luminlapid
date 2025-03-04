from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class User(models.Model):
       first_name = models.CharField(max_length=255)
       middle_name = models.CharField(max_length=255, blank=True)
       last_name = models.CharField(max_length=255)
       email = models.EmailField(max_length=511)
       phone_number = PhoneNumberField(blank=True)  # using PhonenumberField from the third-party package
       joined_date = models.DateField()

# class Visit(models.Model):
#        user = models.ForeignKey(User, on_delete=models.CASCADE)
#        visit_date = models.DateField()
#        visit_time = models.TimeField()
#        visit_duration = models.DurationField()
#        visit_purpose = models.TextField(blank=True)