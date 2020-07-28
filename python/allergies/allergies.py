class Allergies(object):

    allergy_items = ['eggs', 'peanuts', 'shellfish', 'strawberries',
    'tomatoes', 'chocolate', 'pollen', 'cats']
    def __init__(self, score):
        self.score = score
        self.score_binary = list(reversed(list("{0:b}".format(self.score % 256))))

    def allergic_to(self, item):
        item_index = self.allergy_items.index(item)
        if item_index >= len(self.score_binary):
            return False
        return self.score_binary[item_index] == '1'

    @property
    def lst(self):
        lst = []
        for i in range(len(self.score_binary)):
            if self.score_binary[i] == '0':
                continue
            lst.append(self.allergy_items[i])
        return lst

