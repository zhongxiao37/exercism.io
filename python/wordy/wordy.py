import re

OPERATIONS = {
    'plus': '+',
    'minus': '-',
    'multiplied by': '*',
    'divided by': '/'
  }

def answer(question):
    question_exp = []
    last_element_is_operator = True
    m = re.match(r'.*?(-?\d+.*-?\d*)\?', question)
    if not m:
        raise ValueError('unknown question')
    question_list = m.group(1).split(' ')

    while len(question_list) > 0:
        g = question_list.pop(0)
        if re.match('-?\d+', g):
            if last_element_is_operator:
                question_exp.append(g)
                last_element_is_operator = False
            else:
                raise ValueError('last element is number, operator is expected')
        else:
            while len(question_list) > 0 and not re.match('-?\d+', question_list[0]):
                g = g + ' ' + question_list.pop(0)
            if g in OPERATIONS.keys():
                question_exp.append(OPERATIONS[g])
                last_element_is_operator = True
            else:
                raise ValueError('unknown operator')

        if len(question_exp) == 3:
            question_exp = [str(eval(''.join(question_exp)))]
    if len(question_exp) > 1:
        raise ValueError('incomplete operation')

    return int(float(question_exp[0]))
