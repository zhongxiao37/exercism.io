def rectangles(strings):
    all_slots = [[cell for cell in list(row)] for row in strings]
    slots = []
    rectangles = []
    for i, e in enumerate(strings):
        for j, s in enumerate(list(e)):
            # i => row index, j => column index
            if s == '+':
                slots.append((i, j))

    # use a, b, c, d for 4 slots of a rectangle
    for a in slots:
        for b in [slot for slot in slots if slot[0] == a[0] and slot[1] > a[1]]:
            for c in [slot for slot in slots if slot[1] == a[1] and slot[0] > a[0]]:
                for d in [slot for slot in slots if slot[0] - b[0] == c[0] - a[0] and slot[1] - c[1] == b[1] - a[1]]:
                    rectangles.append((a,b,c,d))

    return len([rec for rec in rectangles if is_valid(rec, all_slots)])

def is_valid(rectangle, all_slots):
    a, b, c, d = rectangle
    if all(all_slots[i][j] in ['-', '+'] for j in range(a[1]+1, b[1]) for i in [a[0], c[0]]):
        if all(all_slots[m][n] in ['|', '+'] for m in range(a[0]+1, c[0]) for n in [a[1], b[1]]):
            return True
    
    return False