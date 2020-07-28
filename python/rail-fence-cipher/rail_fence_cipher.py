from itertools import cycle, chain
import re

def encode(message, num):
    rails = arrange_message_to_rails(message, num)
    
    return ''.join([''.join(filter(lambda e: e != None, x)) for x in rails])

def decode(encoded_message, num):
    rails = arrange_message_to_rails(re.sub('.', '?', encoded_message), num)
    encoded_message_list = list(encoded_message)
    decoded_message_list = []
    for i, j in ([i, j] for i in range(len(rails)) for j in range(len(rails[0]))):
        if rails[i][j] == '?':
            rails[i][j] = encoded_message_list.pop(0)

    for row, col in rails_iterator(rails):
        decoded_message_list.append(rails[row][col])
    
    return ''.join(decoded_message_list)
    

def arrange_message_to_rails(message, num):
    rails = [[None for _ in range(len(message))] for __ in range(num)]
    message_list = list(message)
    for row, col in rails_iterator(rails):
        rails[row][col] = message_list.pop(0)
    
    return rails

def rails_iterator(rails):
    cols = list(range(len(rails[0])))
    for j in cycle(chain(range(len(rails)), range(len(rails) - 2, 0, -1))):
        if len(cols) == 0:
            return
        yield j, cols.pop(0)
