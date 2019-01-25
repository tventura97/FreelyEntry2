from django.shortcuts import render
from .models import Entry
from django.utils import timezone
from .forms import EntryForm
from django.shortcuts import redirect
# Create your views here.
def getEntries(request):
    current_user = request.user
    current_number = current_user.getNumber()
    entries = Entry.objects.filter(created_at__lte=timezone.now()).order_by('created_at').filter(number__contains=current_number)[::-1]
    context = {'entries':entries ,'number': current_number}
    return render(request, 'feed/entries.html', context)

def newEntry(request):
    current_user = request.user
    number = current_user.getNumber()
    form = EntryForm(request.POST or None)
    date = timezone.now()
    if form.is_valid():
        obj = form.save(commit = False)
        obj.number = number
        obj.save()
        return redirect('/feed')

    context = {
    'form' : form,
    'date' : date
    }
    return render(request, 'feed/newpost.html', context)
