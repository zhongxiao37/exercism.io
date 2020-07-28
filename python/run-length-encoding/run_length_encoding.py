import re

def encode_m(matchobj):
    return f'{len(matchobj.group(0))}{matchobj.group(1)}'

def decode_m(matchobj):
    return f'{matchobj.group(2)}' * int(matchobj.group(1))

def decode(string):
    return re.sub(r'(\d+)(\D)', decode_m, string)


def encode(string):
    return re.sub(r'(\D)\1+', encode_m, string)
