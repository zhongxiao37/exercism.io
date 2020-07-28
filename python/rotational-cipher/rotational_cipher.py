import re

ALPHABETS = list(chr(x) for x in range(ord('a'), ord('z')+1))
ALPHABETS_UPPER = list(chr(x) for x in range(ord('A'), ord('Z')+1))

def rotate(text, key):
    cipher = ALPHABETS[key:] + ALPHABETS[0:key] + ALPHABETS_UPPER[key:] + ALPHABETS_UPPER[0:key]
    TRANSLATION_TABLE = str.maketrans(''.join(ALPHABETS+ALPHABETS_UPPER), ''.join(cipher))
    return re.sub(r'\w', lambda x: x.group().translate(TRANSLATION_TABLE), text)

