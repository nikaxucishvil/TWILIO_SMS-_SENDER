from twilio.rest import Client
import time
# enter accoint sid and auth token from twilio
account_sid = ' TWILIO ACCOUNT SID'
auth_token = ' TWILIO AUTH TOKEN'
client = Client(account_sid, auth_token)
# Enter the number you want to send the SMS
to_number = '+################'
# The number from your Twilo account
from_number = 'TWILIO PHONE NUMBER'
# enter massage
massage_body = input("SMS_TEXT: ")
# send SMS
massage = client.messages.create(
    body=massage_body,
    from_=from_number,
    to=to_number
)      
print("SMS sent")
