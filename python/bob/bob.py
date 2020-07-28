import re

def response(hey_bob):
    words = re.findall(r'[a-zA-Z\d\?]', hey_bob)

    if len(words) == 0:
        return 'Fine. Be that way!'
    
    if words[-1] == '?':
        if len(words) > 1 and all(e.isupper() for e in words[:-1]):
            return 'Calm down, I know what I\'m doing!'
        else:
            return 'Sure.'
    else:
        words_without_numbers = re.findall(r'[a-zA-Z]', hey_bob)
        if len(words_without_numbers) > 0 and all(e.isupper() for e in words_without_numbers):
            return 'Whoa, chill out!'
        else:
            return 'Whatever.'