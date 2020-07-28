def annotate(minefield):
    height = len(minefield)
    if height == 0:
        return minefield
    width = len(minefield[0])
    if width == 0:
        return minefield
    
    if any(len(row) != width for row in minefield):
        raise ValueError('different row length')
    
    minefield = [list(row) for row in minefield]

    for y in range(height):
        for x in range(width):
            if minefield[y][x] != ' ' and minefield[y][x] != '*':
                raise ValueError('invalid char')
            if minefield[y][x] == ' ':
                cnt = get_mine_count(y, x, height, width, minefield)
                if cnt > 0:
                    minefield[y][x] = str(cnt)
    
    return [''.join(row) for row in minefield]

def get_mine_count(y, x, height, width, minefield):
    cnt = 0
    for i in range(-1, 2):
        if y + i < 0 or y + i > height - 1:
            continue
        for j in range(-1, 2):
            if x + j < 0 or x + j > width - 1:
                continue
            if minefield[y + i][x + j] == '*':
                cnt += 1
    return cnt
     