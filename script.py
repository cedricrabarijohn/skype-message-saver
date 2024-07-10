import os
from skpy import Skype
import time
from dotenv import load_dotenv
from datetime import datetime, timedelta
from utils import format_skype_message, escape_newlines, to_snake_case

load_dotenv()

skype_mail = os.getenv("SKYPE_MAIL")
skype_password = os.getenv("SKYPE_PASSWORD")
chat_id = os.getenv("CHAT_ID")
env_output_dir = os.getenv("OUTPUT_DIR")
env_output_file = os.getenv("OUTPUT_FILE")


output_dir = "skype_messages"

sk = Skype(skype_mail, skype_password)
print(sk)
if not chat_id:
    print("CHAT_ID is empty")
else:
    print(f"Your script is now running ... (Press Ctrl + C to stop it anytime)")
    print(f"Newest messages will be logged in {output_dir} folder")
    if chat_id:
        chat = sk.chats[chat_id]
        print(f"Waiting for sent or incoming messages from {chat.user.name}")
    while True and chat_id:
        os.makedirs(output_dir, exist_ok=True)
        messages = chat.getMsgs()
        output_file = "messages.txt"
        if env_output_dir:
            output_dir = env_output_dir
        if env_output_file:
            output_file = env_output_file

        if messages:
            last_message = messages[0]
            sender = sk.contacts[last_message.userId]
            sender_name = sender.name
            if last_message:
                current_time = datetime.now()
                hoursToAdd = 3
                hoursToAdd_env = os.getenv('GMT')
                if hoursToAdd_env:
                    try:
                        hoursToAdd = int(hoursToAdd_env)
                    except:
                        ''
                last_message_time = last_message.time + timedelta(hours=int(hoursToAdd), seconds=10)
                if current_time <= last_message_time:
                    message_content = last_message.content
                    if message_content == '':
                        message_content = '[has deleted a message]'
                    new_message = f"-----------------------------------------\n{sender_name} - [{last_message_time.strftime('%Y-%m-%d %H:%M:%S')}]\n-----------------------------------------\n\n{format_skype_message(message_content)}"
                    output_file = os.path.join(output_dir,f"{to_snake_case(str(chat.user.name))}_{output_file}")
                    
                    if os.path.exists(output_file):
                        with open(output_file, "r") as f:
                            existing_content = f.read()
                    else:
                        existing_content = ""

                    with open(output_file, "w") as f:
                        f.write(new_message + "\n\n==============================================================\n\n" + existing_content)
                        print(f"{current_time} - New message appended to {output_dir}/{output_file}")
        time.sleep(2)