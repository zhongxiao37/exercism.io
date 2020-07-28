def find(search_list, value):
    if len(search_list) <= 0:
        raise ValueError('invalid search list')
    middle = len(search_list) // 2
    if value == search_list[middle]:
        return middle
    elif len(search_list) == 1:
        raise ValueError('not found')
    elif value < search_list[middle]:
        return find(search_list[:middle], value)
    else:
        return middle + find(search_list[middle:], value)
