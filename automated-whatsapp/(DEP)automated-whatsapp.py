import pywhatkit as kit
from datetime import datetime
import os


def send_whatsapp(number: str, msg: str, hour: int, minute: int):
    kit.sendwhatmsg_instantly(f"+{number}", msg, wait_time=1, tab_close=True)


if __name__ == "__main__":
    number = os.getenv("TO_PHONE")
    msg = "Hi! This is an automated message."
    hour = 14
    minute = 0

    send_whatsapp(number, msg, hour, minute)
