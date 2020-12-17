from django.shortcuts import render, get_object_or_404
from meetings.models import Meeting
# Create your views here.
def detail(request,id):
    """
    Return Meeting details
    """
    meeting = get_object_or_404(Meeting, pk=id)
    #meeting = Meeting.objects.get(pk=id)
    return render(request, detail.html, {"meeting":meeting})
