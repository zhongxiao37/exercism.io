SUFFIX = [
    'the house that Jack built',
    'the malt',
    'the rat',
    'the cat',
    'the dog',
    'the cow with the crumpled horn',
    'the maiden all forlorn',
    'the man all tattered and torn',
    'the priest all shaven and shorn',
    'the rooster that crowed in the morn',
    'the farmer sowing his corn',
    'the horse and the hound and the horn'
    ]

PREFIX = [
    'This is',
    'lay in',
    'ate',
    'killed',
    'worried',
    'tossed',
    'milked',
    'kissed',
    'married',
    'woke',
    'kept',
    'belonged to'
    ]



def recite(start_verse, end_verse):
    lyrics = []
    for i in range(start_verse, end_verse + 1):
        lyric = []
        for j in range(i, 0, -1):
            prefix = PREFIX[0] if i == j else 'that ' + PREFIX[j]
            suffix = SUFFIX[j-1] + ('.' if j == 1 else '')
            lyric.append(prefix + ' ' + suffix)
        
        lyrics.append(' '.join(lyric))

    return lyrics

