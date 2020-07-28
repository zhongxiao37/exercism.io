def rebase(input_base, digits, output_base):
    if input_base <= 1 or output_base <= 1:
        raise ValueError('input base should be larger than one')

    num = 0
    output = []
    for i in range(len(digits)):
        if digits[-1-i] < 0 or digits[-1-i] >= input_base:
            raise ValueError('wrong digit')
        num += digits[-1-i] * input_base ** i
    
    if len(digits) == 0 or num == 0:
        return output

    while True:
        quotient = num // output_base
        remainder = num % output_base

        output.append(remainder)
        num = quotient
        
        if quotient == 0:
            break
    output.reverse()
    return output
