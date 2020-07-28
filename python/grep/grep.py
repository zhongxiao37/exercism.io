from collections import namedtuple
import re

def grep(pattern, flags, files):
    grep_lines = []
    for f in files:
        grep_lines += process_single_file(f, pattern, flags)
    return format_results(grep_lines, flags, len(files) > 1)

def process_single_file(file, pattern, flags):
    grep_lines = []
    regex = re.compile(f'.*{pattern}')
    if '-i' in flags:
        regex = re.compile(f'.*{pattern}', flags=re.IGNORECASE)
    
    f = open(file, 'r')
    counter = 1
    for line in f.readlines():
        matched = False
        if '-x' in flags:
            if line.rstrip().lower() == pattern.lower():
                matched = True
        elif regex.match(line):
            matched = True
        
        if '-v' in flags:
            if not matched:
                grep_lines.append(MatchLine(counter, line, file))
        elif matched:
            grep_lines.append(MatchLine(counter, line, file))
        
        counter += 1
    
    return grep_lines

def format_results(lines, flags, include_file_name):
    if '-l' in flags:
        files = []
        for l in lines:
            new_file = l.file_name+'\n'
            if new_file not in files:
                files.append(new_file)

        return ''.join(files)
    elif '-n' in flags:
        if include_file_name:
            return ''.join(['%s:%s:%s' % (l.file_name, l.line_number, l.line_text) for l in lines])
        else:
            return ''.join(['%s:%s' % (l.line_number, l.line_text) for l in lines])
    else:
        if include_file_name:
            return ''.join(['%s:%s' % (l.file_name, l.line_text) for l in lines])
        else:
            return ''.join([l.line_text for l in lines])

MatchLine = namedtuple('MatchLine', 'line_number, line_text, file_name')