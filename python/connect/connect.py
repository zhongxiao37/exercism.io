from itertools import product
import re

class ConnectGame:
    def __init__(self, board):
        self.board = [re.findall(r'\S', line) for line in board.split('\n')]
        self._height = len(self.board)
        self._width = len(self.board[0])

    def get_winner(self):
        if any(path[-1][1] == self._width - 1 for path in self.calculate_path('X')):
            return 'X'
        if any(path[-1][0] == self._height - 1 for path in self.calculate_path('O')):
            return 'O'
        return ''


    def calculate_path(self, player):
        paths = [[slot] for slot in self.start_slots(player)]

        for path in paths:
            while True:
                last_slot = path[-1]
                adjacent_slots = [(x,y) for x, y in self.find_adjacent_slots(last_slot) if self.board[x][y] == player and (x,y) not in path]
                
                if len(adjacent_slots) == 0:
                    break

                if len(adjacent_slots) > 1:
                    for adjacent_slot in adjacent_slots[1:]:
                        new_path = [s for s in path] + [adjacent_slot]
                        paths.append(new_path)
                path.append(adjacent_slots[0])

            if path[-1][0] == self._height - 1 or path[-1][1] == self._width -1:
                break
        
        return paths

    def find_adjacent_slots(self, slot):
        all_slots = [(slot[0] + x, slot[1] + y) for x, y in product([-1,0,1], [-1,0,1]) if x != y]
        return [s for s in all_slots if 0 <= s[0] < self._height and 0 <= s[1] < self._width]

    def start_slots(self, player):
        if player == 'O':
            return [(0, i) for i, e in enumerate(self.board[0]) if e == 'O']
        else:
            return [(i, 0) for i, e in enumerate(self.board) if e[0] == 'X']

