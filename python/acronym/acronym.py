import re

def abbreviate(words):
    return ''.join(x[0].upper() for x in re.findall(r"[a-zA-Z']+", words))
