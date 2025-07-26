from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os


def send_message(number: str, message: str):
    options = Options()
    options.add_argument(r"--user-data-dir=C:\WhatsAppSeleniumProfile")
    options.add_argument("--profile-directory=Default")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)

    driver.get(f"https://web.whatsapp.com/send?phone={number}&text={message}")
    time.sleep(10)

    try:
        input_box = driver.find_element(
            By.XPATH, '//div[@title="Write a message here"]'
        )
        input_box.send_keys(Keys.ENTER)
        print("✅ Message send")
    except Exception as e:
        print("❌ Couldn´t send message:", e)

    time.sleep(5)
    driver.quit()


if __name__ == "__main__":
    number = os.getenv("TO_PHONE")
    message = "Hi! This is an automated message using Selenium"
    send_message(number, message)
