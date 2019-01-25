from django.db.models.signals import post_save
from django.dispatch import receiver
from twilio.rest import Client

from .models import FEUser

#Twilio credentials
SID = 'AC386dbcd830dc6c527ba603d502dda72e'
AuthToken = 'ab4a13eebaf65faf6ed08652b3dc633b'

#Set up Twilio client
client = Client(SID, AuthToken)

TwilioNumber = '+17325323718'

@receiver(post_save, sender=FEUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print('user created.')
        print('user details: ' + instance.getFirstName())
        receiver = '+1' + instance.getNumber()
        message = client.messages \
                        .create(
                             body='\nHello, ' + instance.getFirstName(),
                             from_=TwilioNumber,
                             to=receiver
                         )
