import re

class Phone(object):
    def __init__(self, phone_number):
        cleaned_number = re.findall('\d', phone_number)
        if cleaned_number[0] == '1':
            cleaned_number = cleaned_number[1:]
        if int(cleaned_number[0]) < 2 or int(cleaned_number[3]) < 2:
            raise ValueError('Wrong area codes')
        cleaned_number = cleaned_number
        if len(cleaned_number) != 10:
            raise ValueError('Wrong length')
        self.area_code = str.join('', cleaned_number[0:3])
        self.number = str.join('', cleaned_number)
        pass

    def pretty(self):
        return "(%s) %s-%s" % (self.area_code, self.number[3:6], self.number[6:])
