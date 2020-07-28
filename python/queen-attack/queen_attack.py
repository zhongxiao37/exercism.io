class Queen(object):
    def __init__(self, row, column):
        if row not in range(0, 8) or column not in range(0, 8):
            raise ValueError('invalid position')
        
        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError('they are in same position')
        if self.row == another_queen.row or self.column == another_queen.column:
            return True
        if abs(another_queen.row - self.row) == abs(another_queen.column - self.column):
            return True
        
        return False
