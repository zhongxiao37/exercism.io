def saddle_points(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return [{}]

    saddle_points = [] 
    try:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == max(matrix[i]) and matrix[i][j] == min((e[j] for e in matrix)):
                    saddle_points.append({'row': i + 1, 'column': j + 1})
    except IndexError:
        raise ValueError('Irregular matrix')
    
    return saddle_points if len(saddle_points) > 0 else [{}]

