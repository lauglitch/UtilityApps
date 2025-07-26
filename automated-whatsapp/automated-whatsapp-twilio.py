import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

from_whatsapp_number = os.getenv("TWILIO_WHATSAPP_FROM")
to_whatsapp_number = os.getenv("TO_PHONE")

message = client.messages.create(
    body="Hello from Twilio and Python!",
    from_=from_whatsapp_number,
    to=to_whatsapp_number,
)

print(f"Message sent with SID: {message.sid}")
