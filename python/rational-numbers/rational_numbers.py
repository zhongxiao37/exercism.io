from __future__ import division
import math


class Rational(object):
    def __init__(self, numer, denom):
        gcd = math.gcd(abs(numer), abs(denom))
        numer = numer // gcd
        denom = denom // gcd

        if denom < 0:
            numer = numer * -1
            denom = denom * -1
        
        self.numer = numer
        self.denom = denom

    def __eq__(self, other):
        return self.numer == other.numer and (self.numer == 0 or self.denom == other.denom)

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return Rational(self.numer * other.denom + self.denom * other.numer, self.denom * other.denom)

    def __sub__(self, other):
        return Rational(self.numer * other.denom - self.denom * other.numer, self.denom * other.denom)

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return Rational(self.numer * other.denom, self.denom * other.numer)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        if power >= 0:
            return Rational(self.numer ** power, self.denom ** power)
        else:
            return Rational(self.denom ** power, self.numer ** power)

    def __rpow__(self, base):
        return (base ** self.numer) ** (1 / self.denom)
