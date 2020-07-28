def recite(start, take=1):
    songs = []
    for i in range(start, start-take, -1):
        if i < start:
            songs.append('')

        if i > 2:
            songs.append(f'{i} bottles of beer on the wall, {i} bottles of beer.')
            songs.append(f'Take one down and pass it around, {i-1} bottles of beer on the wall.')
        elif i == 2:
            songs.append(f'{i} bottles of beer on the wall, {i} bottles of beer.')
            songs.append(f'Take one down and pass it around, {i-1} bottle of beer on the wall.')
        elif i == 1:
            songs.append(f'{i} bottle of beer on the wall, {i} bottle of beer.')
            songs.append(f'Take it down and pass it around, no more bottles of beer on the wall.')
        else:
            songs.append('No more bottles of beer on the wall, no more bottles of beer.')
            songs.append('Go to the store and buy some more, 99 bottles of beer on the wall.')
    return songs