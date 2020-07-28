import collections

CHARACTER_POINTS = {
        1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
        2: ['D', 'G'],
        3: ['B', 'C', 'M', 'P'],
        4: ['F', 'H', 'V', 'W', 'Y'],
        5: ['K'],
        8: ['J', 'X'],
        10: ['Q', 'Z']
}



def score(word):
    words_count = collections.Counter(word.upper())
    point = 0
    for w, c in words_count.items():
        for k, v in CHARACTER_POINTS.items():
            if w in v:
                point += k * c
                break
    
    return point
