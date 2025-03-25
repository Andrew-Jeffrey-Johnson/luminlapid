from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from activity.models import ActivityModel
from activity.forms import ActivityForm
from django.utils.timezone import localtime

def activity(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ActivityForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
        return HttpResponseRedirect('activity')
    else:
        form = ActivityForm()
        all_activities = ActivityModel.objects.all().values()[::-1]
        for activity in all_activities:
            activity['datetime'] = localtime(activity['datetime'])
            #activity['date'] = localtime(activity['date'])
            #activity['time'] = localtime(activity['time'])
        template = loader.get_template('activity.html')
        context = {
            'form' : form,
            'all_activities' : all_activities,
        }
        return HttpResponse(template.render(context, request))