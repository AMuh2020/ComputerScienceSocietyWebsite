from django.shortcuts import render
from .models import event

# Create your views here.
def events(request):
    event_q = event.objects.all()
    return render(request, 'events/events.html',{"events":event_q})