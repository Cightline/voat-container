import attr
import sendgrid
from sendgrid.helpers.mail import *

# Using python-http-client-2.2.1 sendgrid-4.1.0 from pip. 

# Documentation of SendGrid for Python 
# https://github.com/sendgrid/sendgrid-python

def send_async(message):
    # Need a way to get the API key. 
    api_key = 'api-key'
    sg      = sendgrid.SendGridAPIClient(apikey=api_key)

    source_address      = Email(message.from_)
    destination_address = Email(message.to_)

    mail = Mail(source_address, message.subject, destination_address, message.content)

    response = sg.client.mail.send.post(request_body=mail.get())

    # LOG THE RESPONSE?
    # response.status_code
    # response.body
    # response.headers

    # TRACKING (idk if this is needed per message)
    # https://github.com/sendgrid/sendgrid-python/blob/master/USAGE.md#tracking_settings
