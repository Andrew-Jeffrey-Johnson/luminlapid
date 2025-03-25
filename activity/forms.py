# import form class from django
from django import forms
 
# import GeeksModel from models.py
from activity.models import ActivityModel
 
# create a ModelForm
class ActivityForm(forms.ModelForm):
    
    # specify the name of model to use
    class Meta:
        model = ActivityModel
        fields = ["action"]
        widgets = {
            'action': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }