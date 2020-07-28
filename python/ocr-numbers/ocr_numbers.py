OCR_NUMS = {
    " _ \n| |\n|_|\n   ": "0",
    "   \n  |\n  |\n   ": "1",
    " _ \n _|\n|_ \n   ": "2",
    " _ \n _|\n _|\n   ": "3",
    "   \n|_|\n  |\n   ": "4",
    " _ \n|_ \n _|\n   ": "5",
    " _ \n|_ \n|_|\n   ": "6",
    " _ \n  |\n  |\n   ": "7",
    " _ \n|_|\n|_|\n   ": "8",
    " _ \n|_|\n _|\n   ": "9"
  }

def convert(input_grid):
    if len(input_grid) % 4 != 0:
        raise ValueError('invalid row size')
    if len(input_grid[0]) % 3 != 0:
        raise ValueError('invalid column size')
    row_numbers = []
    for i in range(0, len(input_grid), 4):
        row_numbers.append(convert_row(input_grid[i:i+4]))
    return ','.join(row_numbers)

def convert_row(rows):
    numbers = []
    for j in range(0, len(rows[0]), 3):
        cell_key = '\n'.join([row[j:j+3] for row in rows])
        numbers.append(OCR_NUMS[cell_key] if cell_key in OCR_NUMS.keys() else '?')
    return ''.join(numbers)
