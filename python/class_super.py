class Animal:
    def __init__(self, name):
        self.name = name
    
    def yark(self):
        print(f'Animal {self.name}')
    
    def jump(self):
        print('Animal jumps')

class Dog(Animal):
    def dog_yark(self):
        self.yark()
        print(f'Dog {self.name}')
    
    def jump(self):
        print('Dog jumps')

class Water:
    def yark(self):
        print('Water')

class Bingo(Dog, Water):
    def jump(self):
        super().jump()
        super(Dog, self).jump()
        super(Animal, self).jump()


print(Bingo.__mro__)

animal = Animal('bingo')
animal.yark()

dog = Dog('Donald')
dog.dog_yark()


Bingo('bg').jump()

