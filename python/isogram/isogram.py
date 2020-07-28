import re

def is_isogram(string):
    chars = re.findall(r'\w', string.lower())
    if len(chars) == 0:
        return True
    count_list = {}
    for e in chars:
        if e in count_list:
            count_list[e] += 1
        else:
            count_list[e] = 1
    
    return all(v == 1 for k, v in count_list.items())
