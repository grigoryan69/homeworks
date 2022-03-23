import re
import sys
action = ''


counter = 0
def correct_email(emails):
    try:
        int(emails)

    except ValueError:
        global counter
        global action
        regex_gmail = r'\b[A-Za-z0-9._%+-]+@gmail.com+\b'
        regex_mailru = r'\b[A-Za-z0-9._%+-]+@mail.ru+\b'
        regex_yandexru = r'\b[A-Za-z0-9._%+-]+@yandex.ru+\b'
        
        if not (re.fullmatch(regex_gmail, emails))\
            and not (re.fullmatch(regex_mailru, emails))\
            and not (re.fullmatch(regex_yandexru, emails)):
            return 0

        else:    
            action = emails
            return action
    else:
        return 0
