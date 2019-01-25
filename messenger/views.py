from django.shortcuts import render
from twilio.rest import Client
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from feed.models import Entry
from django.utils import timezone


#Twilio credentials
SID = 'AC386dbcd830dc6c527ba603d502dda72e'
AuthToken = 'ab4a13eebaf65faf6ed08652b3dc633b'

TwilioNumber = '+17325323718'

#Set up Twilio client
client = Client(SID, AuthToken)
# Create your views here.
def sendMessageTest(request):
    current_user = request.user
    current_number = current_user.getNumber()
    message = client.messages \
                    .create(
                         body='\nHi please respond to this message when you get a chance, I\'m testing some functions',
                         from_=TwilioNumber,
                         to='+1' + current_number
                             )
    context = {}
    return render(request, 'messenger/sendMessage.html', context)

@csrf_exempt
def receiveMessage(request):
    entry = request.POST.get('Body', None)
    sender = request.POST.get('From', None)[2::]
    current_time = timezone.now()
    print(entry, sender, current_time)
    obj = Entry(body = entry, created_at = current_time, number = sender)
    obj.save()
    print(obj)
    return HttpResponse(str(entry))
