import re
from html import unescape

def to_snake_case(input_string):
    result = []
    for char in input_string:
        if char.isalnum():
            if char.isupper() and result:
                result.append('_')
                result.append(char.lower())
            elif char.isupper() and not result:
                result.append(char.lower())
            else:
                result.append(char)
        else:
            result.append('_')

    return ''.join(result)
    
def escape_newlines(text):
    return text.replace('\n', '\\n')

def format_skype_message(original_message):
    try:
        pattern = r'<legacyquote>[^<]*</legacyquote>(.*?)<legacyquote>'
        match = re.search(pattern, original_message, re.DOTALL)
        end_quote_index = original_message.rfind("</quote>")

        message_after_quote = original_message[end_quote_index + len("</quote>"):].strip()
        if match and message_after_quote:
            escaped_text = escape_newlines(match.group(1).strip())
            return f"[replying to '{unescape(escaped_text)}'] : \n\n{unescape(message_after_quote)}"
        else:
            return original_message
    except Exception as e:
        print(f"Error processing message: {e}")
        return original_message