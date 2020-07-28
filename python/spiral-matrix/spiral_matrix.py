from itertools import cycle

def spiral_matrix(size):
    if size <= 0:
        return []
    matrix = [['' for x in range(size)] for y in range(size)]
    directions = cycle([(0,1), (1,0), (0,-1), (-1,0)])
    visited_slots = [(0, 0)]
    matrix[0][0] = counter = 1
    for direct in directions:
        while True:
            next_slot = (visited_slots[-1][0] + direct[0], visited_slots[-1][1] + direct[1])
            if 0 <= next_slot[0] < size and 0 <= next_slot[1] < size and next_slot not in visited_slots:
                counter += 1
                matrix[next_slot[0]][next_slot[1]] = counter
                visited_slots.append(next_slot)
            else:
                break

        if len(visited_slots) == size ** 2:
            break

    return matrix