import os
from dotenv import load_dotenv
from skpy import Skype, SkypeChat

load_dotenv()

skype_mail = os.getenv("SKYPE_MAIL")
skype_password = os.getenv("SKYPE_PASSWORD")

sk = Skype(skype_mail, skype_password)

for contact in sk.contacts:
    print(f"Chat ID : {contact.chat.id} | Username : {contact.name}")