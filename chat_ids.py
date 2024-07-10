import os
from dotenv import load_dotenv
from skpy import Skype, SkypeChat

load_dotenv()

skype_mail = os.getenv("SKYPE_MAIL")
skype_password = os.getenv("SKYPE_PASSWORD")

sk = Skype(skype_mail, skype_password)

for chat_id in sk.chats.recent():
    chat = sk.chats.chat(chat_id)
    
    try:
        if isinstance(chat, SkypeChat) and chat.userId:
            username = chat.userId
            try:
                username = sk.contacts[username].name
            except:
                username = 'Unknown'
            print(f"Chat ID: {chat_id} | Username: {username}")
    except:
        ''