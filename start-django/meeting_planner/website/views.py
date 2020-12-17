from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting


def welcome(request):
    return render(request, "welcome.html", {"message":"This data from view to template","num_meetings":str(Meeting.objects.count())})       
def date(request):
    """
    Handle request and return current time
    """
    return HttpResponse("Current time is:" + str(datetime.now()))
def about (request):
    return HttpResponse('Text about')