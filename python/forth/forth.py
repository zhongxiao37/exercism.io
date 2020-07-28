import re

class StackUnderflowError(Exception):
    pass


def evaluate(input_data):
    input_data = [e.lower() for e in input_data]
    stack = []
    user_def_operations = {}
    regex = re.compile(': (.+?) (.*) ;', flags=re.IGNORECASE)
    
    for line in input_data:
        m = regex.match(line)
        if m:
            if m.group(1).isdigit():
                raise ValueError('could not redefine number')
            else:
                user_def_operations[m.group(1)] = [user_def_operations[v][0]
                                                    if v in user_def_operations.keys()
                                                    else v
                                                    for v in m.group(2).split(' ')]
        else:
            for e in input_data[-1].split(' '):
                if e.isdigit():
                    stack.append(int(e))
                else:
                    if e in user_def_operations.keys():
                        for op in user_def_operations[e]:
                            stack = evaluate_core(stack, op)
                    else:
                        stack = evaluate_core(stack, e)

    return stack        


def evaluate_core(stack, operator):
    if operator in ['*', '+', '-', '/']:
        if len(stack) >= 2:
            b = stack.pop()
            a = stack.pop()
            new_value = int(eval(operator.join([str(a), str(b)])))
            stack.append(new_value)
        else:
            raise StackUnderflowError('less than 2 elements in stack')
    elif operator in ['dup', 'drop']:
        if len(stack) >= 1:
            if operator == 'dup':
                stack.append(stack[-1])
            elif operator == 'drop':
                stack.pop()
        else:
            raise StackUnderflowError('less than 1 elements in stack')
    elif operator in ['swap', 'over']:
        if len(stack) >= 2:
            if operator == 'swap':
                b = stack.pop()
                a = stack.pop()
                stack.append(b)
                stack.append(a)
            elif operator == 'over':
                stack.append(stack[-2])
        else:
            raise StackUnderflowError('less than 1 elements in stack')
    else:
        stack.append(int(operator))
    return stack