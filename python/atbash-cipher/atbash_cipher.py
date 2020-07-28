import re

ALPHABETS = list(chr(x) for x in range(ord('a'), ord('z')+1))
TRANSLATION_TABLE = str.maketrans(''.join(ALPHABETS), ''.join(reversed(ALPHABETS)))

def encode(plain_text):
    translated_string = [ch.translate(TRANSLATION_TABLE) for ch in re.findall(r'\w', plain_text.lower())]
    return ' '.join([''.join(translated_string[i:i+5]) for i in range(0, len(translated_string), 5)])

def decode(ciphered_text):
    return ''.join([ch.translate(TRANSLATION_TABLE) for ch in re.findall(r'\w', ciphered_text.lower())])

