from django.shortcuts import render
from .models import Entry
from django.utils import timezone

# Create your views here.
def getEntries(request):
    current_user = request.user
    number = current_user.getNumber()
    entries = Entry.objects.filter(created_at__lte=timezone.now()).order_by('created_at')
    context = {'entries':entries ,'number': number}
    return render(request, 'feed/entries.html', context)

def newEntry(request):
    current_user = request.user
    number = current_user.getNumber()
    context = {
    'number' : number,
    'Entry' : Entry
    }
    return render(request, 'feed/newpost.html', context)
