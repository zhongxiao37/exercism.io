import re

def count_words(sentence):
    words_count = {}
    words = re.findall(r"[a-zA-Z\d]+(?:'?[a-zA-Z\d]+)?", sentence.lower())
    for word in words:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1
    
    return words_count
