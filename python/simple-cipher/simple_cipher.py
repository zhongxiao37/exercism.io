import random
from string import ascii_lowercase

class Cipher(object):
    def __init__(self, key=None):
        if key == None:
            self.key = self.new_key()
        else:
            self.key = key

    def encode(self, text):
        encoded_characters = []
        for i in range(0, len(text)):
            ch = list(text)[i]
            ch_index = self.alphabets().index(ch)
            key_index = self.alphabets().index(list(self.key)[i % len(self.key)])
            new_index = (ch_index + key_index % 26) % 26
            encoded_characters.append(chr(97 + new_index))
        return ''.join(encoded_characters)


    def decode(self, text):
        decoded_characters = []
        for i in range(0, len(text)):
            ch = list(text)[i]
            ch_index = self.alphabets().index(ch)
            key_index = self.alphabets().index(list(self.key)[i % len(self.key)])
            new_index = (ch_index - key_index % 26) % 26
            decoded_characters.append(chr(97 + new_index))
        return ''.join(decoded_characters)

    def new_key(self):
        return ''.join([chr(random.randrange(97, 122)) for i in range(100)])
    
    def alphabets(self):
        return list(ascii_lowercase)