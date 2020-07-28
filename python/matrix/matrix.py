class Matrix(object):
    def __init__(self, matrix_string):
        self.data = []
        for row in matrix_string.split('\n'):
            self.data.append(list(map(lambda x: int(x), row.split(' '))))

    def row(self, index):
        return self.data[index-1]

    def column(self, index):
        col_data = []
        for col in self.data:
            col_data.append(col[index-1])
        return col_data