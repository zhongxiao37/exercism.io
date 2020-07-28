import re
import math

def cipher_text(plain_text):
    normalize_plaintext = re.findall(r'\w', plain_text.lower())
    if len(normalize_plaintext) == 0:
        return ''
    col_len = calculate_cols(normalize_plaintext)
    plaintext_segments = []
    for i in range(0, len(normalize_plaintext), col_len):
        plaintext_segments.append(normalize_plaintext[i:i+col_len])

    cipher_segments = [ [] for i in range(col_len)]
    for i in range(0, col_len):
        for row in plaintext_segments:
            if i < len(row):
                cipher_segments[i].append(row[i])
            else:
                cipher_segments[i].append(' ')

    return ' '.join(map(lambda x: ''.join(x), cipher_segments))


def calculate_cols(text):
    col_len = math.floor(math.sqrt(len(text)))
    row_len = len(text) // col_len
    if col_len * row_len < len(text):
        col_len += 1
    if col_len - row_len > 1:
        col_len -= 1
    if col_len < row_len:
        col_len += 1

    return col_len