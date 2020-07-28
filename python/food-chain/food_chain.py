def recite(start_verse, end_verse):
    food_chain = ['fly', 'spider', 'bird', 'cat', 'dog', 'goat', 'cow', 'horse']
    song = []
    song_line_two = [
      '',
      '',
      'How absurd to swallow a ',
      'Imagine that, to swallow a ',
      'What a hog, to swallow a ',
      'Just opened her throat and swallowed a ',
      'I don\'t know how she swallowed a '
    ]

    for i in range(start_verse, end_verse+1):
        foods = food_chain[:i]
        foods.reverse()
        for food_idx, food in enumerate(foods):
            if food_idx == 0:
                song.append(f"I know an old lady who swallowed a {food}.")
                if i > 2 and i < len(food_chain):
                    song.append(f"{song_line_two[i-1]}{food}!")
            elif i > 2 and food_idx < i - 1 and i < len(food_chain):
                a_song = f"She swallowed the {foods[food_idx - 1]} to catch the {food}"
                if food_idx < i - 2:
                    a_song += '.'
                else:
                    a_song += ' that wriggled and jiggled and tickled inside her.'
                song.append(a_song)
            elif i < len(food_chain):
                if i == 2:
                    song.append("It wriggled and jiggled and tickled inside her.")
            
        
        if 1 < i < len(food_chain):
            song.append("She swallowed the spider to catch the fly.")
        if i == len(food_chain):
            song.append("She's dead, of course!")
        else:
            song.append("I don't know why she swallowed the fly. Perhaps she'll die.")
        if i < end_verse:
            song.append("")
        
    
    return song


