import re

def translate(text):
    return ' '.join([translate_core(t) for t in text.split()])
        

def translate_core(text):
    vowel_characters = ['a', 'e', 'i', 'o', 'u', 'yt', 'xr']
    consonant_characters = ['qu', 'ch', 'thr', 'th', 'rh', 'squ', 'sch']

    for vowel in vowel_characters:
        m = re.match(f'^({vowel})(.*)', text)
        if m:
            return m.group() + 'ay'
    
    for consonant in consonant_characters:
        m = re.match(f'^({consonant})(.*)', text)
        m1 = re.match(f'^({consonant})y(.*)', text)
        if m:
            return m.group(2) + m.group(1) + 'ay'
        if m1:
            return 'y' + m1.group(1) + m.group(2) + 'ay'
    
    m = re.match('(.)(.*)', text)
    return m.group(2) + m.group(1) + 'ay'