from string import ascii_lowercase
import math, re

ALPHABET = list(ascii_lowercase)
ALPHABET_LEN = 26

def valid_keys(func):
    def decorator(*args):
        _, a, b = args
        if math.gcd(a, ALPHABET_LEN) != 1:
            raise ValueError(f'invalid key a: {a}')
        return func(*args)
    return decorator



@valid_keys
def encode(plain_text, a, b):
    def encode_char(char):
        if char.isalpha():
            x = ALPHABET.index(char)
        else:
            return char 
        y = (a * x + b) % ALPHABET_LEN
        return ALPHABET[y]
    
    encoded_chars = [encode_char(s) for s in re.findall(r'\w', plain_text.lower())]
    encoded_chars_len = len(encoded_chars)
    return ' '.join([''.join(encoded_chars[i:(min(encoded_chars_len, i+5))])
                             for i in range(0, encoded_chars_len, 5)])

@valid_keys
def decode(ciphered_text, a, b):
    mmi = next(n for n in range(1, ALPHABET_LEN+1) if a * n % ALPHABET_LEN == 1)
    def decode_char(char):
        try:
            y = ALPHABET.index(char)
        except ValueError:
            return char
        x = mmi * (y - b) % ALPHABET_LEN
        return ALPHABET[x]
    return ''.join([decode_char(s) for s in re.findall(r'\w', ciphered_text)])