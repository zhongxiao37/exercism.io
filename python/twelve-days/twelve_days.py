LYRICS = {
    'first': 'a Partridge in a Pear Tree.',
    'second': 'two Turtle Doves,',
    'third': 'three French Hens,',
    'fourth': 'four Calling Birds,',
    'fifth': 'five Gold Rings,',
    'sixth': 'six Geese-a-Laying,',
    'seventh': 'seven Swans-a-Swimming,',
    'eighth': 'eight Maids-a-Milking,',
    'ninth': 'nine Ladies Dancing,',
    'tenth': 'ten Lords-a-Leaping,',
    'eleventh': 'eleven Pipers Piping,',
    'twelfth': 'twelve Drummers Drumming,'
}


def recite(start_verse, end_verse):
    all_lyrics = []
    for n in range(start_verse, end_verse + 1):
        if n == 1:
            lyrics = 'On the first day of Christmas my true love gave to me: {}'.format(LYRICS['first'])
        else:
            lyrics_list = [['first', 'and ' + LYRICS['first']]]
            for i, e in enumerate(LYRICS.items()):
                if i >= n:
                    break
                elif i > 0:
                    lyrics_list.append(e)

            lyrics = ''
            last_lyrics = lyrics_list.pop()
            for i in range(0, len(lyrics_list)):
                ly = lyrics_list[-1-i]
                lyrics = lyrics + ' ' + ly[-1]
            lyrics = 'On the {} day of Christmas my true love gave to me: {}'.format(last_lyrics[0], last_lyrics[-1]) + lyrics

        all_lyrics.append(lyrics)
    return all_lyrics

