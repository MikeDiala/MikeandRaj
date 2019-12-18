from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC20e03af4762ca29e7cbbf7d4ac4dfbb2'
auth_token = '1b36703ae4a0ab09af5dc73203454c47'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_='+14159415730',
         to='+15038258879'
     )

print(message.sid)