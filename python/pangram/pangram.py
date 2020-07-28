import re

def is_pangram(sentence):
    characters = re.findall(r'[a-z]', sentence.lower())
    dic = { k:1 for k in characters }

    if len(dic) == 26:
        return True
    return False