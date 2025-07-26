# Automation of messages in WhatsApp

## Deprecated Files

- `automated-whatsapp.py` (DEPRECATED)  
- `automated-whatsapp-selenium.py` (DEPRECATED)  

## Functional File

- `automated-whatsapp-twilio.py`

---

## Description

This project provides a script to send WhatsApp messages automatically using Twilio's API.

---

## Setup

1. Create a `.env` file in the root of the project folder.  
2. Add the following sensitive variables to the `.env` file:
  - TWILIO_ACCOUNT_SID=your_account_sid_here
  - TWILIO_AUTH_TOKEN=your_auth_token_here
  - TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886

Change `your_account_sid_here` and `your_auth_token_here` to your Twilio credentials.

---

## Use

Run the functional script with:

```bash
python automated-whatsapp-twilio.py
