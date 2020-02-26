from twilio.rest import TwilioRestClient
from twilio.rest import Client

account_sid = "ACb61b99b4011303f21054eee6933acc1a"
auth_token = "6065520f74f36a6cda80c7855406530f"
client = Client(account_sid, auth_token)

message = client.messages \
	            .create(
		body ="Lo hice :)    att- Joshua", # mensaje
		to = "+529935164296", # remplazamos con nuestro numero o al que queramos enviar el sms
		from_= "+12023356732") # el numero que nos asigno twilio

print(message.sid)