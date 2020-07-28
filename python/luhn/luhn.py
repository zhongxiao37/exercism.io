import re
class Luhn(object):
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        if (len(re.findall(r'[^\d\s]', self.card_num))) > 0:
            return False

        card_num = re.findall(r'\d', self.card_num)[::-1]

        if len(card_num) <= 1:
            return False
        
        sum_of_card_num = 0
        for i in range(len(card_num)):
            if i % 2 == 0:
                num = int(card_num[i])
            else:
                num = int(card_num[i]) * 2
                if num > 9:
                    num = num - 9
            sum_of_card_num += num
        
        return sum_of_card_num % 10 == 0

        