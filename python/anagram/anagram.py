def find_anagrams(word, candidates):
    sorted_word = sorted(list(word.lower()))
    anagram = list(filter(lambda x: sorted(list(x.lower())) == sorted_word and x.lower() != word.lower(), candidates))
    return anagram

