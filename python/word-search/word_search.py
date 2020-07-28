from itertools import chain, permutations 

class Point(object):
    def __init__(self, x, y):
        self.x = None
        self.y = None

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch(object):
    def __init__(self, puzzle):
        self._puzzle = [list(row) for row in puzzle]
        self._height = len(puzzle)
        self._width = len(puzzle[0])

    def search(self, word):
        reversed_word = word[::-1]
        # calculate all 8 directions by (col, row)
        directions = [(col, row) for col in [-1, 0, 1] for row in [-1, 0, 1]]
        directions.remove((0, 0))
        # calculate all border points and uniq them
        border_points = [(border, row) for border in (0, self._width - 1) for row in range(self._height)]
        border_points += [(col, border) for border in (0, self._height - 1) for col in range(self._width)]
        border_points = set(border_points)

        for point in border_points:
            for direct in directions:
                pointer = list(point)
                words = []
                while True:
                    words.append(self._puzzle[pointer[1]][pointer[0]])
                    if 0 <= pointer[1] + direct[1] < self._height and 0 <= pointer[0] + direct[0] < self._width:
                        pointer = [pointer[0] + direct[0], pointer[1] + direct[1]]
                    else:
                        break
                words = ''.join(words)
                if word in words:
                    index = words.find(word)
                    start_point = Point(point[0] + direct[0] * index, point[1] + direct[1] * index)
                    end_point = Point(point[0] + direct[0] * (index + len(word) - 1), point[1] + direct[1] * (index + len(word) - 1))
                    return (start_point, end_point)

        return None