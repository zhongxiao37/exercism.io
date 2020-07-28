from collections import deque
import re

BRACKETS = {
    '}': '{',
    ']': '[',
    ')': '('
}

def is_paired(input_string):
    wrong_bracket = False
    queue = deque([])
    for s in input_string:
        m = re.match(r'[\[\(\{]', s)
        n = re.match(r'[\]\)\}]', s)
        if m:
            queue.append(m.group())
        elif n:
            if len(queue) > 0 and queue[-1] == BRACKETS[n.group()]:
                queue.pop()
            else:
                wrong_bracket = True
    
    return len(queue) == 0 and not wrong_bracket