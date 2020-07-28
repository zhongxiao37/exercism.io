def roman(number):
    roman_num_dict = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }

    quotient_list = []
    formatted_quotient_list = []

    for k, v in roman_num_dict.items():
        while number >= v:
            quotient_list.append(k * (number // v))
            number = number - v * (number // v)
    
    while len(quotient_list) > 0:
        current_item = quotient_list.pop()
        if len(current_item) <= 3:
            formatted_quotient_list.insert(0, current_item)
        elif len(quotient_list) == 0:
            # for case IIII, if no item is found before IIII, we need to change it to IV
            idx = list(roman_num_dict.keys()).index(current_item[0])
            ahead_key = list(roman_num_dict.keys())[idx-1]
            formatted_quotient_list.insert(0, ahead_key)
            formatted_quotient_list.insert(0, current_item[0])
        else:
            item_before_current_item = quotient_list.pop()
            # for case IIII, if one item is found before IIII
            idx = list(roman_num_dict.keys()).index(current_item[0])
            idx_ = list(roman_num_dict.keys()).index(item_before_current_item[0])

            if idx - idx_ > 1:
                # for case IIII, if X is found before IIII, we need to change it to XIV
                ahead_key = list(roman_num_dict.keys())[idx-1]
                quotient_list.append(item_before_current_item)
            else:
                # for case IIII, if V is found before IIII, we need to change it to IX
                ahead_key = list(roman_num_dict.keys())[idx_-1]

            formatted_quotient_list.insert(0, ahead_key)
            formatted_quotient_list.insert(0, current_item[0])
    
    return ''.join(formatted_quotient_list)