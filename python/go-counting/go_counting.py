from itertools import permutations, product
from functools import reduce
from operator import itemgetter, add

BLACK = 'B'
WHITE = 'W'
NONE = 'N'
DIRECTIONS = ((-1,0), (0,-1), (1,0), (0,1))


class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):
        self._board = [list(row) for row in board]
        self._height = len(self._board)
        self._width = len(self._board[0])

    def territory(self, x, y):
        """Find the owner and the territories given a coordinate on
           the board

        Args:
            x (int): Column on the board
            y (int): Row on the board

        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
        """
        owners = set()
        walked_slots = set()
        if x < 0 or y < 0 or self._width <= x or self._height <= y:
            raise ValueError('Exceed the board')
        if self._board[y][x] == ' ':
            # find nearby blank slots
            walked_slots.add((x, y))
            nearby_slots = self.find_nearby_slots(x, y)
            for a, b in nearby_slots:
                if (a, b) in walked_slots:
                    continue
                else:
                    nearby_slots += self.find_nearby_slots(a, b)
                    walked_slots.add((a,b))
            # find the owner
            for a, b in walked_slots:
                for direction in DIRECTIONS:
                    [owners.add(self._board[n][m])
                    for m, n in Walker(self._board, a, b, direction)
                    if self._board[n][m] != ' ']
        
        if len(owners) == 1:
            owner = BLACK if 'B' in owners else WHITE
            return owner, walked_slots
        else:
            return NONE, walked_slots

                

    def territories(self):
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        owners = {BLACK: set(), WHITE: set(), NONE: set()}
        for y in range(self._height):
            for x in range(self._width):
                if self._board[y][x] == ' ':
                    owner, slot_territory = self.territory(x, y)
                    owners[owner] = owners[owner].union(slot_territory)
        
        return owners


    def find_nearby_slots(self, x, y):
        nearby_slots = []
        for direction in DIRECTIONS:
            new_point = tuple(sum(e) for e in list(zip((x, y), direction)))
            if 0 <= new_point[1] < self._height and 0 <= new_point[0] < self._width:
                if self._board[new_point[1]][new_point[0]] == ' ':
                    nearby_slots.append(new_point)
        
        return nearby_slots
        


class Walker:
    def __init__(self, board, x, y, direction):
        self._board = board
        self._point = (x, y)
        self._direction = direction
    
    def __iter__(self):
        return self
    
    def __next__(self):
        point = self._point
        self._point = tuple(sum(e) for e in list(zip(self._point, self._direction)))
        if 0 <= point[1] < len(self._board) and 0 <= point[0] < len(self._board[0]):
            point_value = self._board[point[1]][point[0]]
            if point_value == 'B' or point_value == 'W':
                self._point = (-1, -1)
            return point
        else:
            raise StopIteration
        

