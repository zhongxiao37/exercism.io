class CustomSet(object):
    def __init__(self, elements=[]):
        self.elements = list(elements)

    def isempty(self):
        return len(self.elements) == 0

    def __contains__(self, element):
        return any(e == element for e in self.elements)

    def issubset(self, other):
        return all(i in other for i in self.elements)

    def isdisjoint(self, other):
        return self.intersection(other).isempty()

    def __eq__(self, other):
        return sorted(self.elements) == sorted(other.elements)

    def add(self, element):
        if element not in self.elements:
            self.elements.append(element)

    def intersection(self, other):
        intersection = [i for i in self.elements if i in other]
        return self.__class__(intersection)

    def __sub__(self, other):
        return self.__class__([i for i in self.elements if i not in other])

    def __add__(self, other):
        return self.__class__(self.elements + [i for i in other.elements if i not in self])
