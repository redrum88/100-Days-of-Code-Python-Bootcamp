from twilio.rest import Client

from_number = "+14258421421"  # Enter your Twilio Phone Number
to_number = "+447759xxxxxx"  # Enter your Phone Number

account_sid = "TWILIO SID"  # Twilio SID
auth_token = "TWILIO AUTH KEY"  # Twilio Auth Key


class NotificationManager():

    def __init__(self, messages):
        self.client = Client(account_sid, auth_token)
        message = self.client.messages \
            .create(
            body=messages,
            from_=from_number,
            to=to_number
        )
        print(message.sid)

    pass
