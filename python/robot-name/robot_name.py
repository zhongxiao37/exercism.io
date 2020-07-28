import random

class Robot(object):
    def __init__(self):
        self.generate_name()

    def reset(self):
        self.generate_name()

    def generate_name(self):
        random.seed()
        self.name = chr(random.randrange(65, 90)) + \
                    chr(random.randrange(65, 90)) + \
                    chr(random.randrange(48, 57)) + \
                    chr(random.randrange(48, 57)) + \
                    chr(random.randrange(48, 57))
