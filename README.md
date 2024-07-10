# SKYPE MESSAGE SAVER

## Intro
This project aims to save messages logs from a skype account into a text file in your computer

> Nb : In my case, I'm using "python3" alias to run the python scripts, so feel free to use any existing alias in your current OS like "py" or "py3".

## Installation
```sh
pip install -r requirements.txt
```
## Environment variables
Please copy content from **.env-local** into a new file named **.env**.

And then edit values corresponding to your personnal settings

-  **SKYPE_MAIL** : The email or username of your skype account (mandatory)

- **SKYPE_PASSWORD** : Your password (mandatory)
- **CHAT_ID** : The id of the chat you're trying to get logs from (just leave it blank for the moment) (mandatory)

**Other environment variables**

- **OUTPUT_DIR** : The directory where your file will be stored (facultative) (by default "skype_messages")
- **OUTPUT_FILE** : The file where your results will be writen to (facultative) (by default "messages.txt")
- **GMT** : A number defining your GMT time (for example if you have a gmt + 3 , the right value would be 3) (facultative) (by default 3)

## Usage
### Get chat ids with usernames (excluding group chats)
```sh
python3 chat_ids.py
```
This script will prompt you a list of your current discussions in your skype account

**Output example**
```
Chat ID: 8:live:.cid.588a589c92azd39c | Username: John Doe
Chat ID: 28:e7a9407c-2467-5551-9546-70081f4eaazd5 | Username: Crim
Chat ID: 8:live:.cid.8726e84e7108azddb | Username: Hanlee Sn
```
### Edit CHAT_ID value in your .env file
Once you have your list, you copy the targeted id and paste it as a value of your CHAT_ID variable

**Example if you take John Doe as your target, your value would look like**
```
CHAT_ID=8:live:.cid.675a869c9ecce50c
```

### Launch the script
Now that you are all set up, launch the script using this command
```
python3 script.py
```

## View the results
Go to the directory and open the file to see incoming messages (By default, it's in "skype_messages/messages.txt")

# Conclusion
Meow.