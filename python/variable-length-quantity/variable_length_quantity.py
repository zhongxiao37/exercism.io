def encode(numbers):
    encoded_numbers = []
    for num in numbers:
        num_bin = format(num, 'b')
        num_bin_slice = []
        for i in range(len(num_bin), 0, -7):
            seven_bit_num = int(num_bin[max(0, i-7):i], 2)
            if i == len(num_bin):
                num_bin_slice.append(seven_bit_num)
            else:
                num_bin_slice.append(128 + seven_bit_num)
        num_bin_slice.reverse()
        encoded_numbers += num_bin_slice
    return encoded_numbers


def decode(bytes_):
    decoded_numbers = []
    temp_binary = ''
    for num in bytes_:
        if num > 127:
            num -= 128
            temp_binary += format(num, '07b')
        else:
            temp_binary += format(num, '07b')
            decoded_numbers.append(int(temp_binary, 2))
            temp_binary = ''
    
    if len(temp_binary) > 0:
        raise ValueError('incomplete sequence')
        
    return decoded_numbers
