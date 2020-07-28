def append(list1, list2):
    for e in list2:
        list1.append(e)
    return list1


def concat(lists):
    list1 = []
    for l in lists:
        list1 = append(list1, l)
    return list1


def filter(function, list):
    list1 = []
    for e in list:
        if function(e):
            list1.append(e)
    return list1


def length(list):
    counter = 0
    for e in list:
        counter += 1
    return counter


def map(function, list):
    list1 = []
    for e in list:
        list1.append(function(e))
    return list1


def foldl(function, list, initial):
    _sum = initial
    for e in list:
        _sum = function(_sum, e)
    return _sum


def foldr(function, list, initial):
    _sum = initial
    for e in reversed(list):
        _sum = function(e, _sum)
    return _sum


def reverse(list):
    return [list[i] for i in range(len(list)-1, -1, -1)]
