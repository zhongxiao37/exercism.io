def reverse(text):
    text_list = list(text)
    text_list.reverse()
    return str.join('', text_list)
