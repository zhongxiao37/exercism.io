import re
import itertools
import string

def solve(puzzle):
    #匹配出所有字母，转为大写
    words = re.findall('[A-Z]+', puzzle.upper())
    #将字母放到集合里
    unique_chars = set(''.join(words))
    #因为数字只有10个，所以如果字母大于10个就会出错
    assert len(unique_chars) <= 10, 'Too many letters'
    #将式子的首字母排到前面，方便判断首字母是否为0
    first_letters = {word[0] for word in words}
    n = len(first_letters)
    sorted_chars = ''.join(first_letters) + \
        ''.join(unique_chars - first_letters)
    #所有数字
    digits = '0123456789'
    zero = digits[0]
    #获取所有数字的全排列
    for guess in itertools.permutations(digits, len(sorted_chars)):
        #所有式子的首字母都不能为0
        if zero not in guess[:n]:
            #将字母替换为数字
            trans = str.maketrans(sorted_chars, ''.join(guess))
            equation = puzzle.translate(trans)
            #如果数字式子的计算结果正确
            if eval(equation):
                return dict(zip(sorted_chars, [int(i) for i in guess]))
    
    return None