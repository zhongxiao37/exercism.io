import math

class ComplexNumber(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        if self.real == other.real and self.imaginary == other.imaginary:
            return True
        else:
            return False

    def __add__(self, other):
        return self.__class__(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return self.__class__(self.real * other.real - self.imaginary * other.imaginary,
                              self.real * other.imaginary + self.imaginary * other.real)

    def __sub__(self, other):
        return self.__class__(self.real - other.real, self.imaginary - other.imaginary)

    def __truediv__(self, other):
        real = (self.real * other.real + self.imaginary * other.imaginary) * 1.00 / (other.real ** 2 + other.imaginary ** 2)
        imaginary = (self.imaginary * other.real - self.real * other.imaginary) * 1.00 / (other.real ** 2 + other.imaginary ** 2)
        return self.__class__(real, imaginary)

    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imaginary ** 2)

    def conjugate(self):
        return self.__class__(self.real, -1 * self.imaginary)

    def exp(self):
        if self.imaginary == math.pi:
            real = math.e ** self.real * -1
            imaginary = math.e ** self.real * 0
            return self.__class__(real, imaginary)
        elif self.imaginary == 0:
            real = math.e ** self.real * 1
            imaginary = math.e ** self.real * 0
            return self.__class__(real, imaginary)
