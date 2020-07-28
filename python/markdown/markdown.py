import re


def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    for i in lines:
        m = re.match('(#*) (.*)', i)
        if m:
            i = '<h{}>{}</h{}>'.format(len(m.group(1)), m.group(2), len(m.group(1))) 
        i = re.sub(r'__([^\n]+?)__', r'<strong>\1</strong>', i)
        i = re.sub(r'_([^\n]+?)_', r'<em>\1</em>', i)

        m = re.match(r'\* (.*)', i)
        if m:
            i = '<li>' + m.group(1) + '</li>'
            if not in_list:
                in_list = True
                i = '<ul>' + i
        else:
            if in_list:
                res += '</ul>'
                in_list = False

        m = re.match('<h|<ul|<p|<li', i)
        if not m:
            i = '<p>' + i + '</p>'

        res += i
    if in_list:
        res += '</ul>'
    return res
